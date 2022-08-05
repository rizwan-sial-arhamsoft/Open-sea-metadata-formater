import pandas as pd
import json

df = pd.read_excel('TraitsS2.xlsx',
                   usecols=['Background', 'Body', 'Frame', 'Corner', 'Border', 'Full Head', 'Mouth', 'Eyes', 'Crown',
                            'Mask', 'Snout', 'HandsOpen', 'HandsClosed', 'Object'])

print(df)
print(df['Background'].iloc[0].find("No"))
row_1 = []
for i in range(0, 10000):
    row_1 = []
    if df['Background'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Background', 'value': df['Background'].iloc[i]})
    if df['Body'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Body', 'value': df['Body'].iloc[i]})
    if df['Frame'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Frame', 'value': df['Frame'].iloc[i]})
    if df['Corner'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Corner', 'value': df['Corner'].iloc[i]})
    if df['Border'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Border', 'value': df['Border'].iloc[i]})
    if df['Full Head'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Full Head', 'value': df['Full Head'].iloc[i]})
    if df['Mouth'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Mouth', 'value': df['Mouth'].iloc[i]})
    if df['Eyes'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Eyes', 'value': df['Eyes'].iloc[i]})
    if df['Crown'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Crown', 'value': df['Crown'].iloc[i]})
    if df['Mask'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Mask', 'value': df['Mask'].iloc[i]})
    if df['Snout'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Snout', 'value': df['Snout'].iloc[i]})
    if df['HandsOpen'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'HandsOpen', 'value': df['HandsOpen'].iloc[i]})
    if df['HandsClosed'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'HandsClosed', 'value': df['HandsClosed'].iloc[i]})
    if df['Object'].iloc[i].find("No") == -1:
        row_1.append({'trait_type': 'Object', 'value': df['Object'].iloc[i]})
    print(row_1)
    data = {
        "name": f"Image#{i}",
        "description": "Ethnology Series 2: Gods and Demons is a collection of 10,000 NFTs authentically and "
                       "inclusively derived from the world's religions."
                       "Hand-drawn by artist and professor Pablo Garcia, the diversity of art is unparalleled. Each "
                       "has been assigned an alignment from Chaotic Evil to Lawful Good. "
                       "Series 1 and 2 NFTs will serve as tickets to Ethnology's Bridge of Fate blockchain game, "
                       "hosted on our website [[hyperlink]], in which you can compete to win big Eth prizes. "
                       "Also try our NFT based governance to vote on how the treasury is spent and check out our "
                       "featured artists gallery.",
        "image": f"ipfs://QmXKUNj8XfduGBJ545WQexWTwyTuhJodrif5f3R34JjFTE/S2_{str(i + 1).rjust(5, '0')}.png",
        "attributes": row_1}
    with open(f'Jason-Data/{i}.json', 'w') as fp:
        json.dump(data, fp)
