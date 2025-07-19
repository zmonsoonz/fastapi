from fastapi import FastAPI
import uvicorn

app = FastAPI()

links_data = [
    {
        "id": 1,
        "title": "GitHub",
        "url": "https://github.com/zmonsoonz",
        "image": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
    },
    {
        "id": 2,
        "title": "Telegram",
        "url": "https://t.me/@d.mokrov",
        "image": "https://telegram.org/img/t_logo.png"
    },
    {
        "id": 3,
        "title": "Mail",
        "url": "mok-danil28@mail.ru",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.vecteezy.com%2Fvector-art%2F21009957-mail-vector-icon-black-letter-icon-email-message-linear-icon-vector-illustration&psig=AOvVaw25-FAmTi2mDwjJtFb4YNYh&ust=1753047251936000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCOjQx4fwyY4DFQAAAAAdAAAAABAE"
    }
]

@app.get("/links")
def get_links():
    return links_data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)