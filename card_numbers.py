from itertools import combinations
from collections import Counter
import polars as pl

def lists_with_sum(total: int, n_items: int) -> list[list[int]]:
    return [
        list(combo)
        for combo in combinations(range(1, total + 1), n_items)
        if sum(combo) == total
    ]

def find_unique_by_position(
    i_vals: list[list[int]],
    i_pos: int
) -> tuple[list[list[int]], list[list[int]]] :
    pos_vals = [l[i_pos] for l in i_vals]
    print(pos_vals)
    counts = Counter(pos_vals)
    once = [x for x in pos_vals if counts[x] == 1]
    l_bad = [
        row for row in i_vals
        if row[i_pos] in once
    ]
    l_ok = [
        row for row in i_vals
        if row[i_pos] not in once
    ]
    return l_bad, l_ok

def display_md(i_df: pl.DataFrame):
    print(i_df.to_pandas().to_markdown(index=False))

def analyze(
    i_sum: int,
    i_participants: list[str]
):
    print("These are all the possible combinations:\n")
    all_combos = lists_with_sum(i_sum, 3)
    df_1 = pl.DataFrame(
        all_combos,
        schema=i_participants,
        orient="row"
    )
    df_1 = (
        df_1
        .with_columns(
            pl.int_range(1, pl.len()+1).alias("Seq")
        )
        .select(["Seq"] + i_participants)
    )
    print(df_1.to_pandas().to_markdown(index=False))
    p = i_participants[0]
    print(f"""
Now let's take a look at what cards for a {p} would generate a unique possibility.
Those need to be excluded because {p} does not know what the others got.
    """)
    df_unique_p = (
        df_1
        .sort(p)
        .with_columns(
            pl.col(p).count().over(p).alias("dups")
        )
        .filter(pl.col("dups") == 1)
        .drop("dups")
        .sort("Seq")
    )
    display_md(df_unique_p)
    
    drop_seqs = set()
    drop_seqs.update(df_unique_p.select("Seq").to_series().to_list())
    df_rem = (
        df_1
        .filter(
            ~(pl.col("Seq").is_in(drop_seqs))
        )
    )
    print("\nRemaining\n")
    display_md(df_rem)
    print("\n")

    p2 = i_participants[1]
    p2_no = (
        df_unique_p
        .select(p2)
        .unique()
        .to_series()
        .to_list()
    )
    p2_no_list = ",".join([str(l) for l in p2_no])
    drop_seqs_list = ",".join([str(l) for l in list(drop_seqs)])
    print(f"""
Now {p2} says that he/she already knew that {p} didn't know. That means that
{p2} knows that {p} couldn't have {drop_seqs_list}.
Note that, {p2} had {p2_no_list} in when {p} had {drop_seqs_list}.
Therefore {p2} could not be sure beforehand that {p} didn't know all if he had {p2_no_list}.
So we will also eliminate cases when {p2} has {p2_no_list}.
    """)
    df_rem_2 = (
        df_rem
        .filter(
            (~pl.col(p2).is_in(p2_no))
        )
    )
    display_md(df_rem_2)

    print(f"""
{p2} also doesn't know all the numbers. So we will have to find and eliminate all original cases
where {p2} had a number unique to all possibilities. These are:
    """)
    df_unique_p2 = (
        df_1
        .sort(p2)
        .with_columns(
            pl.col(p2).count().over(p2).alias("dups")
        )
        .filter(pl.col("dups") == 1)
        .drop("dups")
        .sort("Seq")
    )
    display_md(df_unique_p2)

    print("""
After excluding these, we are left with:
    """)
    df_rem_2 = (
        df_rem_2
        .join(
            df_unique_p2,
            on="Seq",
            how="anti"
        )
    )
    display_md(df_rem_2)

    p3 = i_participants[2]
    print(f"""
At this, {p3} says that he/she knows all the numbers now, implying she did not know before.
So, we will also eliminate all possibilities from the original set where {p3}'s number was
unique. Those are:
    """)
    df_unique_p3 = (
        df_1
        .sort(p3)
        .with_columns(
            pl.col(p3).count().over(p3).alias("dups")
        )
        .filter(pl.col("dups") == 1)
        .drop("dups")
        .sort("Seq")
    )
    display_md(df_unique_p3)
    print("""
So, now we are left with:
    """)
    df_rem_3 = (
        df_rem_2
        .join(
            df_unique_p3,
            on="Seq",
            how="anti")
    )
    display_md(df_rem_3)
    if df_rem_3.height == 1:
        print("\nWe are left with just one possibility, which is the answer")
        return
    print(f"""
We have multiple possibilities still left. But if among these one number for {p3}
indicate a unique possibility, that would work. Because at this point {p3} knows.
    """)
    df_unique_p3_final = (
        df_rem_3
        .sort(p3)
        .with_columns(
            pl.col(p3).count().over(p3).alias("dups")
        )
        .filter(pl.col("dups") == 1)
        .drop("dups")
        .sort("Seq")
    )
    if df_unique_p3_final.height > 0:
        display_md(df_unique_p3_final)
        return
    print("No such cases")
