from enum import Enum
from queue import Queue
from doubly_linked_list import DoublyLinkedList, Node


class State(Enum):
    Increasing = 1
    Decreasing = -1


def is_report_safe(levels_list: DoublyLinkedList, problem_dampened=False):
    report_state = None
    current_level: Node = levels_list.head
    while current_level.next is not None:
        previous_level = current_level
        current_level = current_level.next
        level_state = check_level_state(previous_level.data, current_level.data)
        if report_state is None:
            report_state = level_state
        level_safe = verify_level_safety(
            level_state, report_state, previous_level, current_level
        )

        if not level_safe:
            if not problem_dampened:
                first_culprit = previous_level.prev
                second_culprit = previous_level
                third_culprit = current_level
                if first_culprit:
                    levels_list.remove(first_culprit)
                    report_safe = is_report_safe(levels_list, problem_dampened=True)
                    if report_safe:
                        print("Report safe by removing first culprit!")
                        return True
                    else:
                        levels_list.insert(first_culprit.data, first_culprit.prev)
                levels_list.remove(second_culprit)
                report_safe = is_report_safe(levels_list, problem_dampened=True)
                if report_safe:
                    print("Report safe by removing second culprit!")
                    return True
                else:
                    levels_list.insert(second_culprit.data, second_culprit.prev)
                levels_list.remove(third_culprit)
                report_safe = is_report_safe(levels_list, problem_dampened=True)
                if report_safe:
                    print("Report safe by removing third culprit!")
                    return True
                else:
                    return False
            else:
                return False
    return True


def create_levels_list(levels: list[str]):
    levels_list = DoublyLinkedList()
    current_level: Node = None
    for level in levels:
        new_level = levels_list.insert(int(level), current_level)
        current_level = new_level
    return levels_list


def check_level_state(previous_level, current_level):
    if previous_level == current_level:
        level_state = None
    elif previous_level > current_level:
        level_state = State.Decreasing
    else:
        level_state = State.Increasing
    return level_state


def verify_level_safety(
    level_state, report_state, previous_level: Node, current_level: Node
):
    if (
        level_state is None
        or (level_state == State.Increasing and report_state == State.Decreasing)
        or (level_state == State.Decreasing and report_state == State.Increasing)
        or (
            abs(previous_level.data - current_level.data) > 3
            or abs(previous_level.data - current_level.data) < 1
        )
    ):
        return False
    return True


def main():
    reports = open("reports.txt")
    safe_reports = 0
    for report in reports:
        levels_strings = report.split(" ")
        levels_list = create_levels_list(levels_strings)
        safe_report = is_report_safe(levels_list)
        if safe_report:
            safe_reports += 1
    print("Safe Reports: " + str(safe_reports))


main()
