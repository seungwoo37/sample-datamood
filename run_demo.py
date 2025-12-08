# run_demo.py
from pathlib import Path
from datamood.mood_sorter import MoodSorter


def show(result: dict) -> None:
    """
    MoodSorter.analyze()가 반환한 결과 dict를
    사람이 보기 좋게 포맷팅해서 출력하는 함수.
    """
    print("\n=== 결과 ===")

    # 최상위 요약 정보
    print("입력 타입:", result.get("type"))
    print("감정 레이블:", result.get("emotion_label"))

    raw = result.get("raw") or {}

    # 메타데이터들 (있을 때만 출력)
    if "title" in raw:
        print("제목:", raw["title"])
    if "url" in raw:
        print("URL :", raw["url"])

    if "percentage" in raw and "score" in raw:
        print(f"점수/백분율: {raw['score']} / {raw['percentage']}")

    # 텍스트 미리보기 (앞 100자만)
    preview = raw.get("text")
    if preview:
        preview = preview[:100].replace("\n", " ")
        print("텍스트 미리보기:", preview, "...")

    print("====================\n")


def main():
    # 1) 감정 분석기 준비
    ms = MoodSorter()

    # 2) 현재 파일(run_demo.py) 기준으로 예제 파일 경로 설정
    base_dir = Path(__file__).resolve().parent
    examples_dir = base_dir / "examples"

    # 3) 한 번에 돌릴 4가지 입력
    inputs = [
        # 1) 텍스트 파일
        str(examples_dir / "tst1.txt"),

        # 2) 오디오 파일 (WAV)
        str(examples_dir / "하늘에계신우리아버지.wav"),

        # 3) 유튜브 URL
        "https://www.youtube.com/shorts/XrKXrqeXq4Q",

        # 4) 기사(텍스트) URL
        "https://biz.newdaily.co.kr/site/data/html/2025/12/04/2025120400106.html",
    ]

    # 4) 순서대로 분석 실행
    for item in inputs:
        print(f"\n>>> 분석 시작: {item}")
        try:
            result = ms.analyze(item)
        except Exception as e:
            print("⚠ 분석 중 오류 발생:", e)
            continue

        show(result)


if __name__ == "__main__":
    main()
