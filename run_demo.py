# run_demo.py
from pathlib import Path
from datamood.mood_sorter import MoodSorter


def show(result: dict) -> None:
    print("\n=== 결과 ===")
    print("입력 타입:", result.get("type"))
    print("감정 레이블:", result.get("emotion_label"))

    raw = result.get("raw") or {}
    if "title" in raw:
        print("제목:", raw["title"])
    if "url" in raw:
        print("URL :", raw["url"])

    if "percentage" in raw and "score" in raw:
        print(f"점수/백분율: {raw['score']} / {raw['percentage']}")

    preview = raw.get("text") or raw.get("recognized_text")
    if preview:
        preview = preview[:100].replace("\n", " ")
        print("텍스트 미리보기:", preview, "...")

    if result.get("saved_txt_path"):
        print("저장된 텍스트 파일:", result["saved_txt_path"])
    if result.get("sorted_path"):
        print("정렬된 파일 경로:", result["sorted_path"])

    print("====================\n")


def main():
    ms = MoodSorter()

    base_dir = Path(__file__).resolve().parent
    examples_dir = base_dir / "examples"

    inputs = [
        str(examples_dir / "tst1.txt"),
        "https://www.youtube.com/shorts/81hs3IW6GdQ",
        
        str(examples_dir / "하늘에계신우리아버지.wav"),
        
        "https://biz.newdaily.co.kr/site/data/html/2025/12/04/2025120400106.html",
    ]

    for item in inputs:
        print(f"\n>>> 분석 + 정렬 시작: {item}")
        try:
            result = ms.analyze_and_sort(item, base_dir, move=False)
        except Exception as e:
            print("⚠ 처리 중 오류 발생:", e)
            continue

        show(result)


if __name__ == "__main__":
    main()
