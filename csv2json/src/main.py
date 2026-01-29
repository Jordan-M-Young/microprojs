import argparse
from utils import check_file_or_dir, check_file_format
from constants import FileFormats, CheckOutput, JSON2CSV, CSV2JSON
import transforms as TR


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("transform", help="display a square of a given number")
    parser.add_argument("input", help="input file or dir")
    parser.add_argument("output", help="output file or dir")
    parser.add_argument(
        "--headers",
        help="use if transforming from csv to json, does your csv have headers? if yes -> 1 if not -> 0",
    )

    args = parser.parse_args()

    header_flag = True
    if args.headers:
        print(args.headers)

    input = args.input
    output = args.output

    input_check = check_file_or_dir(input)
    output_check = check_file_or_dir(output)

    input_format = None
    output_format = None

    if input_check == CheckOutput.DNE:
        print(f"input: {input} does not exist or cannot be found.")
        return 0
    if output_check == CheckOutput.DNE:
        print(f"output: {output} does not exist or cannot be found.")
        return 0

    if input_check == CheckOutput.FILE:
        input_format = check_file_format(input)

    if output_check == CheckOutput.FILE:
        output_format = check_file_format(output)

    if args.transform == CSV2JSON:
        if input_format == FileFormats.JSON or input_format == FileFormats.OTHER:
            print(
                f"input format: {input_format} not supported for {CSV2JSON} transform"
            )
            return 0

        if output_format == FileFormats.CSV or output_format == FileFormats.OTHER:
            print(f"output format: {output} not supported for {CSV2JSON} transform")
            return 0

        if input_format == FileFormats.CSV and output_format == FileFormats.JSON:
            data = TR.load_json(input)
            if args.headers == "0":
                header_flag = False
            json_data = TR.csv_to_json(data, has_headers=header_flag)
            TR.write_json(output, json_data)

    elif args.transform == JSON2CSV:
        if input_format == FileFormats.CSV or input_format == FileFormats.OTHER:
            print(
                f"input format: {input_format} not supported for {JSON2CSV} transform"
            )
            return 0

        if output_format == FileFormats.JSON or output_format == FileFormats.OTHER:
            print(f"output format: {output} not supported for {JSON2CSV} transform")
            return 0

        if output_format == FileFormats.CSV:
            TR.json_to_csv(input, output)
            return 1

        print(f"Input {input} & Output {output} are valid for the {JSON2CSV} transform")

    else:
        print(
            f"transform not supported. Valid transform values are {CSV2JSON} or {JSON2CSV}"
        )


if __name__ == "__main__":
    main()
