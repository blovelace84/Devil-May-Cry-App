def load_custom_css():
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exocet:wght@400;500;600;700&display=swap');

    body {
        background-color: #111111;
        color: #eeeeee;
        font-family: 'Exocet', serif;
    }
    .title {
        color: #ff4500;
        font-size: 60px;
        text-shadow: 2px 2px 8px #000000;
        letter-spacing: 2px;
        margin-bottom: 20px;
        text-align: center;
    }
    .header {
        color: #ffd700;
        font-size: 36px;
        padding-bottom: 15px;
        border-bottom: 2px solid #4a4a4a;
        margin-bottom: 30px;
        text-align: center;
    }
    .section {
        margin-bottom: 60px;
    }
    .character-name {
        color: #ff8c00;
        font-size: 36px;
        margin-top: 30px;
        text-shadow: 1px 1px 2px #000000;
    }
    .weapon-name {
        color: #b22222;
        font-size: 30px;
        margin-top: 20px;
        text-shadow: 1px 1px 2px #000000;
    }
    .enemy-name {
        color: #adff2f;
        font-size: 30px;
        margin-top: 20px;
        text-shadow: 1px 1px 2px #000000;
    }
    .lore-title {
        color: #87CEFA;
        font-size: 30px;
        margin-top: 20px;
        text-shadow: 1px 1px 2px #000000;
    }
    .button {
        background-color: #ff4500;
        color: #eeeeee;
        font-size: 24px;
        padding: 12px 30px;
        border: 2px solid #c81e1e;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease;
        margin-top: 20px;
        box-shadow: 2px 2px 5px #000000;
        font-family: 'Exocet', serif;
    }
    .button:hover {
        background-color: #c81e1e;
        color: #ffffff;
        box-shadow: 3px 3px 7px #000000;
    }
    .container {
        padding: 40px;
        border-radius: 15px;
        background-color: rgba(0, 0, 0, 0.7);
        margin-bottom: 30px;
    }
    .image-display {
        border: 4px solid #c81e1e;
        border-radius: 10px;
        box-shadow: 2px 2px 5px #000000;
        margin-bottom: 20px;
    }
    </style>
    """