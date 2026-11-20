import logging
from datetime import datetime
from pathlib import Path

from Data import *

from strategies.Strategy1_Stock_Trade import run as run_s1
from strategies.Market_Rigem_Strategy import run as run_market_regime
from strategies.Market_Aware_Stock_Strategy import run as run_market_aware
from strategies.Benchmark import run as run_benchmark

# --------------------------------
# Logging
# --------------------------------

OUTPUT_DIR = Path("outputs")
LOG_DIR = OUTPUT_DIR / "logs"

LOG_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOG_DIR / "pipeline.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# --------------------------------
# Main Pipeline
# --------------------------------

def main():

    start_time = datetime.now()

    logger.info("=" * 50)
    logger.info("CANADIAN ML TRADING PIPELINE STARTED")
    logger.info("=" * 50)

    try:

        # 1. Load Data
        logger.info("Loading project data...")

        # data = load_all_data()

        logger.info("Data loaded successfully.")

        # 2. Strategy 1
        logger.info("Running Strategy 1...")

        stock_results = run_s1()

        print(stock_results["strategy1_results"])

        logger.info("Strategy 1 completed.")

        # 3. Market Regime
        logger.info("Running Market Regime Model...")

        market_results = run_market_regime()

        print(market_results["market_results"])

        logger.info("Market Regime completed.")

        # 4. Market-Aware Strategy + Benchmark
        logger.info("Running Market-Aware Strategy...")

        market_aware_results = run_market_aware( )


        print(market_aware_results["strategy2_results"])


        logger.info("Market-Aware Strategy completed.")

        # 5.  Benchmark
        logger.info("Running Benchmark...")

        benchmark_results = run_benchmark( )


        print(benchmark_results["benchmark_comparison"])


        logger.info("Benchmark completed.")


        # 6. Finish
        elapsed = datetime.now() - start_time

        logger.info("=" * 50)
        logger.info("PIPELINE COMPLETED SUCCESSFULLY")
        logger.info("Execution Time: %s", elapsed)
        logger.info("=" * 50)

        all_results = {
            "strategy1": stock_results,
            "market_regime": market_results,
            "market_aware": market_aware_results
            }

        return all_results

    except Exception:

        logger.exception("PIPELINE FAILED")

        raise


if __name__ == "__main__":
    main()