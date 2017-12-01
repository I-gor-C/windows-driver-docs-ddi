---
UID: NE.ntddrilapitypes.RIL3GPPCALLCONTROLCAUSECODE
title: RIL3GPPCALLCONTROLCAUSECODE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\ril3gppcallcontrolcausecode.htm
old-project: netvista
ms.assetid: a469e292-a57d-4876-a050-266f57985a50
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RIL3GPPCALLCONTROLCAUSECODE
req.alt-loc: ntddrilapitypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# RIL3GPPCALLCONTROLCAUSECODE enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RIL3GPPCALLCONTROLCAUSECODE { 
  RIL_3GPPCCCAUSE_NO_ROUTE_TO_DESTINATION,
  RIL_3GPPCCCAUSE_CHANNEL_UNACCEPTABLE,
  RIL_3GPPCCCAUSE_OPERATOR_DETERMINED_BARRING,
  RIL_3GPPCCCAUSE_NORMAL_CALL_CLEARING,
  RIL_3GPPCCCAUSE_USER_BUSY,
  RIL_3GPPCCCAUSE_NO_USER_RESPONDING,
  RIL_3GPPCCCAUSE_USER_ALERTING_NO_ANSWER,
  RIL_3GPPCCCAUSE_CALL_REJECTED,
  RIL_3GPPCCCAUSE_NUMBER_CHANGED,
  RIL_3GPPCCCAUSE_PREEMPTION,
  RIL_3GPPCCCAUSE_DESTINATION_OUT_OF_ORDER,
  RIL_3GPPCCCAUSE_INVALID_NUMBER_FORMAT,
  RIL_3GPPCCCAUSE_FACILITY_REJECTED,
  RIL_3GPPCCCAUSE_RESPONSE_TO_STATUS_ENQUIRY,
  RIL_3GPPCCCAUSE_NORMAL_UNSPECIFIED,
  RIL_3GPPCCCAUSE_NO_CHANNEL_AVAILABLE,
  RIL_3GPPCCCAUSE_NETWORK_OUT_OF_ORDER,
  RIL_3GPPCCCAUSE_TEMPORARY_FAILURE,
  RIL_3GPPCCCAUSE_CONGESTION,
  RIL_3GPPCCCAUSE_ACCESS_INFORMATION_DISCARDED,
  RIL_3GPPCCCAUSE_REQUESTED_CHANNEL_NOT_AVAILABLE,
  RIL_3GPPCCCAUSE_RESOURCE_UNAVAILABLE_UNSPECIFIED,
  RIL_3GPPCCCAUSE_QOS_UNAVAILABLE,
  RIL_3GPPCCCAUSE_FACILITY_NOT_SUBSCRIBED,
  RIL_3GPPCCCAUSE_INCOMING_CALLS_BARRED_IN_CUG,
  RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AUTHORIZED,
  RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AVAILABLE,
  RIL_3GPPCCCAUSE_SVC_NOT_AVAILABLE_UNSPECIFIED,
  RIL_3GPPCCCAUSE_BEARER_SERVICE_NOT_IMPLEMENTED,
  RIL_3GPPCCCAUSE_ACM_NOT_LESS_THAN_ACMMAX,
  RIL_3GPPCCCAUSE_FACILITY_NOT_IMPLEMENTED,
  RIL_3GPPCCCAUSE_ONLY_RESTRICTED_DIGITAL_BEARER,
  RIL_3GPPCCCAUSE_SVC_NOT_IMPLEMENTED_UNSPECIFIED,
  RIL_3GPPCCCAUSE_INVALID_TRANSACTION_ID,
  RIL_3GPPCCCAUSE_USER_NOT_MEMBER_OF_CUG,
  RIL_3GPPCCCAUSE_INCOMPATIBLE_DESTINATION,
  RIL_3GPPCCCAUSE_SEMANTICALLY_INCORRECT_MESSAGE,
  RIL_3GPPCCCAUSE_INVALID_MANDATORY_FUNCTION,
  RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_IMPLEMENTED,
  RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_COMPATIBLE,
  RIL_3GPPCCCAUSE_IE_NOT_IMPLEMENTED,
  RIL_3GPPCCCAUSE_CONDITIONAL_IE_ERROR,
  RIL_3GPPCCCAUSE_MESSAGE_NOT_COMPATIBLE,
  RIL_3GPPCCCAUSE_RECOVERY_ON_TIMER_EXPIRY,
  RIL_3GPPCCCAUSE_PROTOCOL_ERROR_UNSPECIFIED,
  RIL_3GPPCCCAUSE_INTERWORKING_UNSPECIFIED
} RIL3GPPCALLCONTROLCAUSECODE;
````


## -enum-fields
<dl>

### -field <a id="RIL_3GPPCCCAUSE_NO_ROUTE_TO_DESTINATION"></a><a id="ril_3gppcccause_no_route_to_destination"></a><b>RIL_3GPPCCCAUSE_NO_ROUTE_TO_DESTINATION</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_CHANNEL_UNACCEPTABLE"></a><a id="ril_3gppcccause_channel_unacceptable"></a><b>RIL_3GPPCCCAUSE_CHANNEL_UNACCEPTABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_OPERATOR_DETERMINED_BARRING"></a><a id="ril_3gppcccause_operator_determined_barring"></a><b>RIL_3GPPCCCAUSE_OPERATOR_DETERMINED_BARRING</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NORMAL_CALL_CLEARING"></a><a id="ril_3gppcccause_normal_call_clearing"></a><b>RIL_3GPPCCCAUSE_NORMAL_CALL_CLEARING</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_USER_BUSY"></a><a id="ril_3gppcccause_user_busy"></a><b>RIL_3GPPCCCAUSE_USER_BUSY</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NO_USER_RESPONDING"></a><a id="ril_3gppcccause_no_user_responding"></a><b>RIL_3GPPCCCAUSE_NO_USER_RESPONDING</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_USER_ALERTING_NO_ANSWER"></a><a id="ril_3gppcccause_user_alerting_no_answer"></a><b>RIL_3GPPCCCAUSE_USER_ALERTING_NO_ANSWER</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_CALL_REJECTED"></a><a id="ril_3gppcccause_call_rejected"></a><b>RIL_3GPPCCCAUSE_CALL_REJECTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NUMBER_CHANGED"></a><a id="ril_3gppcccause_number_changed"></a><b>RIL_3GPPCCCAUSE_NUMBER_CHANGED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_PREEMPTION"></a><a id="ril_3gppcccause_preemption"></a><b>RIL_3GPPCCCAUSE_PREEMPTION</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_DESTINATION_OUT_OF_ORDER"></a><a id="ril_3gppcccause_destination_out_of_order"></a><b>RIL_3GPPCCCAUSE_DESTINATION_OUT_OF_ORDER</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INVALID_NUMBER_FORMAT"></a><a id="ril_3gppcccause_invalid_number_format"></a><b>RIL_3GPPCCCAUSE_INVALID_NUMBER_FORMAT</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_FACILITY_REJECTED"></a><a id="ril_3gppcccause_facility_rejected"></a><b>RIL_3GPPCCCAUSE_FACILITY_REJECTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_RESPONSE_TO_STATUS_ENQUIRY"></a><a id="ril_3gppcccause_response_to_status_enquiry"></a><b>RIL_3GPPCCCAUSE_RESPONSE_TO_STATUS_ENQUIRY</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NORMAL_UNSPECIFIED"></a><a id="ril_3gppcccause_normal_unspecified"></a><b>RIL_3GPPCCCAUSE_NORMAL_UNSPECIFIED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NO_CHANNEL_AVAILABLE"></a><a id="ril_3gppcccause_no_channel_available"></a><b>RIL_3GPPCCCAUSE_NO_CHANNEL_AVAILABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_NETWORK_OUT_OF_ORDER"></a><a id="ril_3gppcccause_network_out_of_order"></a><b>RIL_3GPPCCCAUSE_NETWORK_OUT_OF_ORDER</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_TEMPORARY_FAILURE"></a><a id="ril_3gppcccause_temporary_failure"></a><b>RIL_3GPPCCCAUSE_TEMPORARY_FAILURE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_CONGESTION"></a><a id="ril_3gppcccause_congestion"></a><b>RIL_3GPPCCCAUSE_CONGESTION</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_ACCESS_INFORMATION_DISCARDED"></a><a id="ril_3gppcccause_access_information_discarded"></a><b>RIL_3GPPCCCAUSE_ACCESS_INFORMATION_DISCARDED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_REQUESTED_CHANNEL_NOT_AVAILABLE"></a><a id="ril_3gppcccause_requested_channel_not_available"></a><b>RIL_3GPPCCCAUSE_REQUESTED_CHANNEL_NOT_AVAILABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_RESOURCE_UNAVAILABLE_UNSPECIFIED"></a><a id="ril_3gppcccause_resource_unavailable_unspecified"></a><b>RIL_3GPPCCCAUSE_RESOURCE_UNAVAILABLE_UNSPECIFIED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_QOS_UNAVAILABLE"></a><a id="ril_3gppcccause_qos_unavailable"></a><b>RIL_3GPPCCCAUSE_QOS_UNAVAILABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_FACILITY_NOT_SUBSCRIBED"></a><a id="ril_3gppcccause_facility_not_subscribed"></a><b>RIL_3GPPCCCAUSE_FACILITY_NOT_SUBSCRIBED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INCOMING_CALLS_BARRED_IN_CUG"></a><a id="ril_3gppcccause_incoming_calls_barred_in_cug"></a><b>RIL_3GPPCCCAUSE_INCOMING_CALLS_BARRED_IN_CUG</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AUTHORIZED"></a><a id="ril_3gppcccause_bearer_capability_not_authorized"></a><b>RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AUTHORIZED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AVAILABLE"></a><a id="ril_3gppcccause_bearer_capability_not_available"></a><b>RIL_3GPPCCCAUSE_BEARER_CAPABILITY_NOT_AVAILABLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_SVC_NOT_AVAILABLE_UNSPECIFIED"></a><a id="ril_3gppcccause_svc_not_available_unspecified"></a><b>RIL_3GPPCCCAUSE_SVC_NOT_AVAILABLE_UNSPECIFIED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_BEARER_SERVICE_NOT_IMPLEMENTED"></a><a id="ril_3gppcccause_bearer_service_not_implemented"></a><b>RIL_3GPPCCCAUSE_BEARER_SERVICE_NOT_IMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_ACM_NOT_LESS_THAN_ACMMAX"></a><a id="ril_3gppcccause_acm_not_less_than_acmmax"></a><b>RIL_3GPPCCCAUSE_ACM_NOT_LESS_THAN_ACMMAX</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_FACILITY_NOT_IMPLEMENTED"></a><a id="ril_3gppcccause_facility_not_implemented"></a><b>RIL_3GPPCCCAUSE_FACILITY_NOT_IMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_ONLY_RESTRICTED_DIGITAL_BEARER"></a><a id="ril_3gppcccause_only_restricted_digital_bearer"></a><b>RIL_3GPPCCCAUSE_ONLY_RESTRICTED_DIGITAL_BEARER</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_SVC_NOT_IMPLEMENTED_UNSPECIFIED"></a><a id="ril_3gppcccause_svc_not_implemented_unspecified"></a><b>RIL_3GPPCCCAUSE_SVC_NOT_IMPLEMENTED_UNSPECIFIED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INVALID_TRANSACTION_ID"></a><a id="ril_3gppcccause_invalid_transaction_id"></a><b>RIL_3GPPCCCAUSE_INVALID_TRANSACTION_ID</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_USER_NOT_MEMBER_OF_CUG"></a><a id="ril_3gppcccause_user_not_member_of_cug"></a><b>RIL_3GPPCCCAUSE_USER_NOT_MEMBER_OF_CUG</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INCOMPATIBLE_DESTINATION"></a><a id="ril_3gppcccause_incompatible_destination"></a><b>RIL_3GPPCCCAUSE_INCOMPATIBLE_DESTINATION</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_SEMANTICALLY_INCORRECT_MESSAGE"></a><a id="ril_3gppcccause_semantically_incorrect_message"></a><b>RIL_3GPPCCCAUSE_SEMANTICALLY_INCORRECT_MESSAGE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INVALID_MANDATORY_FUNCTION"></a><a id="ril_3gppcccause_invalid_mandatory_function"></a><b>RIL_3GPPCCCAUSE_INVALID_MANDATORY_FUNCTION</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_IMPLEMENTED"></a><a id="ril_3gppcccause_message_type_not_implemented"></a><b>RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_IMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_COMPATIBLE"></a><a id="ril_3gppcccause_message_type_not_compatible"></a><b>RIL_3GPPCCCAUSE_MESSAGE_TYPE_NOT_COMPATIBLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_IE_NOT_IMPLEMENTED"></a><a id="ril_3gppcccause_ie_not_implemented"></a><b>RIL_3GPPCCCAUSE_IE_NOT_IMPLEMENTED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_CONDITIONAL_IE_ERROR"></a><a id="ril_3gppcccause_conditional_ie_error"></a><b>RIL_3GPPCCCAUSE_CONDITIONAL_IE_ERROR</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_MESSAGE_NOT_COMPATIBLE"></a><a id="ril_3gppcccause_message_not_compatible"></a><b>RIL_3GPPCCCAUSE_MESSAGE_NOT_COMPATIBLE</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_RECOVERY_ON_TIMER_EXPIRY"></a><a id="ril_3gppcccause_recovery_on_timer_expiry"></a><b>RIL_3GPPCCCAUSE_RECOVERY_ON_TIMER_EXPIRY</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_PROTOCOL_ERROR_UNSPECIFIED"></a><a id="ril_3gppcccause_protocol_error_unspecified"></a><b>RIL_3GPPCCCAUSE_PROTOCOL_ERROR_UNSPECIFIED</b>

<dd></dd>

### -field <a id="RIL_3GPPCCCAUSE_INTERWORKING_UNSPECIFIED"></a><a id="ril_3gppcccause_interworking_unspecified"></a><b>RIL_3GPPCCCAUSE_INTERWORKING_UNSPECIFIED</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>