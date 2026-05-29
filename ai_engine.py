import os

# 1. 定義 AIGC 核心黃金提示詞矩陣
MODEL_PROMPT = {
    "Subject": "A highly detailed, realistic 25-year-old East Asian female influencer",
    "Appearance": "smiling, long wavy brown hair, natural makeup, sharp focus, capturing intricate facial details",
    "Outfit": "wearing a stylish black V-neck t-shirt and a white pleated skirt",
    "Setting": "sitting at an outdoor cafe on a bustling Tokyo street, blurry background with city lights, cinematic lighting",
    "Quality_Tags": "photorealistic, 8k resolution, highly detailed skin texture, professional photography, masterpiece"
}

# 2. 自動化工作流：建立輸出目錄
output_folder = "AI_Influencer_Output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"[系統訊息] 已自動建立專案輸出資料夾: {output_folder}")

# 3. 輸出提示詞報告檔案
prompt_file_path = os.path.join(output_folder, "ai_generation_prompt.txt")
full_prompt = ", ".join(MODEL_PROMPT.values())

with open(prompt_file_path, "w", encoding="utf-8") as f:
    f.write("【複製以下完整提示詞至你的 AI 生成工具 (如 Midjourney / Stable Diffusion / Gemini)】\n\n")
    f.write(full_prompt)

print("===================================================")
print("[製程完成] 提示詞矩陣已成功封裝！")
print(f"[檔案位置] 請至 {output_folder} 資料夾複製 ai_generation_prompt.txt")
print("===================================================\n")
os.system("pause")