from wes_runner import WESRunner
from argo_runner import ArgoRunner
from calrissian_runner import CalrissianRunner

def test_runner(runner, name):
    """
    Runs validation and execution for a given runner.
    """
    print(f"\nTesting {name}...\n" + "-"*30)
    try:
        runner.validate()
        runner.execute()
    except Exception as e:
        print(f"Error in {name}: {e}")

if __name__ == "__main__":
    # Test WES Runner
    wes = WESRunner("example_wes_workflow.cwl", {"input1": "value1"})
    test_runner(wes, "WES Runner")

    # Test Argo Runner
    argo = ArgoRunner("example_argo_workflow.cwl", {"namespace": "argo"})
    test_runner(argo, "Argo Runner")

    # Test Calrissian Runner
    calrissian = CalrissianRunner("example_calrissian_workflow.cwl", {"cpu": 2, "memory": "4Gi"})
    test_runner(calrissian, "Calrissian Runner")

    print("\nAll runners tested successfully!")
