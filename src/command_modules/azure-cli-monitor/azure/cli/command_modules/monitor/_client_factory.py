# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


# MANAGEMENT CLIENT FACTORIES
def cf_monitor(_):
    from azure.mgmt.monitor import MonitorManagementClient
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    return get_mgmt_service_client(MonitorManagementClient)


def cf_alert_rules(kwargs):
    return cf_monitor(kwargs).alert_rules


def cf_alert_rule_incidents(kwargs):
    return cf_monitor(kwargs).alert_rule_incidents


def cf_autoscale(kwargs):
    return cf_monitor(kwargs).autoscale_settings


def cf_diagnostics(kwargs):
    return cf_monitor(kwargs).diagnostic_settings


def cf_log_profiles(kwargs):
    return cf_monitor(kwargs).log_profiles


def cf_action_groups(kwargs):
    return cf_monitor(kwargs).action_groups


def cf_activity_log_alerts(kwargs):
    return cf_monitor(kwargs).activity_log_alerts


def cf_metrics(kwargs):
    return cf_monitor(kwargs).metrics


def cf_metric_def(kwargs):
    return cf_monitor(kwargs).metric_definitions


def cf_activity_log(kwargs):
    return cf_monitor(kwargs).activity_logs


def cf_event_categories(kwargs):
    return cf_monitor(kwargs).event_categories
