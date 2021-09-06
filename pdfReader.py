from tabula import read_pdf
df =read_pdf("Bodal.pdf",pages=1)[0]
df.to_csv("Bodal1.csv")
print(df)