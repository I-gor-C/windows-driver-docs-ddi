---
UID: NE.rilapitypes.RILDISPLAYINFOTAG
title: RILDISPLAYINFOTAG
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildisplayinfotag_2.htm
old-project: netvista
ms.assetid: 1e9bbf23-8b3e-490f-b225-562a978662fe
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILDISPLAYINFOTAG
req.alt-loc: rilapitypes.h
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
req.product: Windows 10 or later.
---

# RILDISPLAYINFOTAG enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef enum _RILDISPLAYINFOTAG { 
  RIL_EXTENDED_DISPLAY_TAG_SKIP,
  RIL_EXTENDED_DISPLAY_TAG_CONTINUATION,
  RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS,
  RIL_EXTENDED_DISPLAY_TAG_CAUSE,
  RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR,
  RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR,
  RIL_EXTENDED_DISPLAY_TAG_PROMPT,
  RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS,
  RIL_EXTENDED_DISPLAY_TAG_STATUS,
  RIL_EXTENDED_DISPLAY_TAG_INBAND,
  RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS,
  RIL_EXTENDED_DISPLAY_TAG_REASON,
  RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME,
  RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME,
  RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME,
  RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME,
  RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME,
  RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT,
  RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY,
  RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID,
  RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS,
  RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME,
  RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER,
  RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER,
  RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER,
  RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER,
  RIL_EXTENDED_DISPLAY_TAG_TEXT,
  RIL_EXTENDED_DISPLAY_TAG_MAX
} RILDISPLAYINFOTAG;
````


## -enum-fields
<dl>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_SKIP"></a><a id="ril_extended_display_tag_skip"></a><b>RIL_EXTENDED_DISPLAY_TAG_SKIP</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CONTINUATION"></a><a id="ril_extended_display_tag_continuation"></a><b>RIL_EXTENDED_DISPLAY_TAG_CONTINUATION</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS"></a><a id="ril_extended_display_tag_called_address"></a><b>RIL_EXTENDED_DISPLAY_TAG_CALLED_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CAUSE"></a><a id="ril_extended_display_tag_cause"></a><b>RIL_EXTENDED_DISPLAY_TAG_CAUSE</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR"></a><a id="ril_extended_display_tag_progress_indicator"></a><b>RIL_EXTENDED_DISPLAY_TAG_PROGRESS_INDICATOR</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR"></a><a id="ril_extended_display_tag_notification_indicator"></a><b>RIL_EXTENDED_DISPLAY_TAG_NOTIFICATION_INDICATOR</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_PROMPT"></a><a id="ril_extended_display_tag_prompt"></a><b>RIL_EXTENDED_DISPLAY_TAG_PROMPT</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS"></a><a id="ril_extended_display_tag_accumulated_digits"></a><b>RIL_EXTENDED_DISPLAY_TAG_ACCUMULATED_DIGITS</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_STATUS"></a><a id="ril_extended_display_tag_status"></a><b>RIL_EXTENDED_DISPLAY_TAG_STATUS</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_INBAND"></a><a id="ril_extended_display_tag_inband"></a><b>RIL_EXTENDED_DISPLAY_TAG_INBAND</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS"></a><a id="ril_extended_display_tag_calling_address"></a><b>RIL_EXTENDED_DISPLAY_TAG_CALLING_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_REASON"></a><a id="ril_extended_display_tag_reason"></a><b>RIL_EXTENDED_DISPLAY_TAG_REASON</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME"></a><a id="ril_extended_display_tag_calling_party_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_CALLING_PARTY_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME"></a><a id="ril_extended_display_tag_called_party_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_CALLED_PARTY_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME"></a><a id="ril_extended_display_tag_original_called_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME"></a><a id="ril_extended_display_tag_redirecting_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME"></a><a id="ril_extended_display_tag_connected_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT"></a><a id="ril_extended_display_tag_originating_restrict"></a><b>RIL_EXTENDED_DISPLAY_TAG_ORIGINATING_RESTRICT</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY"></a><a id="ril_extended_display_tag_date_time_of_day"></a><b>RIL_EXTENDED_DISPLAY_TAG_DATE_TIME_OF_DAY</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID"></a><a id="ril_extended_display_tag_call_appearance_id"></a><b>RIL_EXTENDED_DISPLAY_TAG_CALL_APPEARANCE_ID</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS"></a><a id="ril_extended_display_tag_feature_address"></a><b>RIL_EXTENDED_DISPLAY_TAG_FEATURE_ADDRESS</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME"></a><a id="ril_extended_display_tag_redirection_name"></a><b>RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NAME</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER"></a><a id="ril_extended_display_tag_redirection_number"></a><b>RIL_EXTENDED_DISPLAY_TAG_REDIRECTION_NUMBER</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER"></a><a id="ril_extended_display_tag_redirecting_number"></a><b>RIL_EXTENDED_DISPLAY_TAG_REDIRECTING_NUMBER</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER"></a><a id="ril_extended_display_tag_original_called_number"></a><b>RIL_EXTENDED_DISPLAY_TAG_ORIGINAL_CALLED_NUMBER</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER"></a><a id="ril_extended_display_tag_connected_number"></a><b>RIL_EXTENDED_DISPLAY_TAG_CONNECTED_NUMBER</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_TEXT"></a><a id="ril_extended_display_tag_text"></a><b>RIL_EXTENDED_DISPLAY_TAG_TEXT</b>

<dd></dd>

### -field <a id="RIL_EXTENDED_DISPLAY_TAG_MAX"></a><a id="ril_extended_display_tag_max"></a><b>RIL_EXTENDED_DISPLAY_TAG_MAX</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>