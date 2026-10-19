from dlt._workspace.cli.requirements import SourceRequirements


def test_installed_dlt_prerelease_without_mutating_requirement() -> None:
    class PrereleaseSourceRequirements(SourceRequirements):
        def current_dlt_version(self) -> str:
            return "1.31.1rc1"

    source = PrereleaseSourceRequirements.from_string("dlt>=1.31")

    assert source.is_installed_dlt_compatible()
    assert source.dlt_requirement.specifier.prereleases is None
