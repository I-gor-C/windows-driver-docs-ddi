---
UID: NF.storport.StorPortEtwEvent2
title: StorPortEtwEvent2
author: windows-driver-content
description: The StorPortEtwEvent2 publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are expressed as two name-value pairs.
old-location: storage\storportetwevent2.htm
ms.assetid: A390D684-C675-4140-8E8E-8330FB3192E4
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: Storage
req.header: storport.h
req.include-header: Storport.h
req.target-type: Universal
req.target-min-winverclnt: Available in starting with Windows 8.1.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortEtwEvent2
req.alt-loc: storport.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: StorPortEtwEvent2
req.iface: 
req.product: Windows 10 or later.
---

# StorPortEtwEvent2 function



## -description
<p>The <b>StorPortEtwEvent2</b> publishes an Event Tracing for Windows (ETW) event to a storage trace channel. The miniport can log two general purpose ETW parameters. The ETW parameters are  expressed as two name-value pairs.</p>


## -syntax

````
ULONG StorPortEtwEvent2(
  _In_     PVOID                     HwDeviceExtension,
  _In_opt_ PSTOR_ADDRESS             Address,
  _In_     ULONG                     EventId,
  _In_     PWSTR                     EventDescription,
  _In_     ULONGLONG                 EventKeywords,
  _In_     STORPORT_ETW_LEVEL        EventLevel,
  _In_     STORPORT_ETW_EVENT_OPCODE EventOpcode,
  _In_opt_ PSCSI_REQUEST_BLOCK       Srb,
  _In_opt_ PWSTR                     Parameter1Name,
  _In_     ULONGLONG                 Parameter1Value,
  _In_opt_ PWSTR                     Parameter2Name,
  _In_     ULONGLONG                 Parameter2Value
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension for the host bus adapter (HBA).</p>
</dd>

### -param <i>Address</i> [in, optional]

<dd>
<p>The storage unit device address. This parameter is NULL for adapter devices.</p>
</dd>

### -param <i>EventId</i> [in]

<dd>
<p>A miniport defined identifier for the ETW event.</p>
</dd>

### -param <i>EventDescription</i> [in]

<dd>
<p>The description text for the event. This text string must be &lt;= STORPORT_ETW_MAX_DESCRIPTION_LENGTH.</p>
</dd>

### -param <i>EventKeywords</i> [in]

<dd>
<p>Keyword flags for event categorization. Set to 0 if no keyword is desired. The keywords are a bitwise OR combination of the following.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="STORPORT_ETW_EVENT_KEYWORD_IO"></a><a id="storport_etw_event_keyword_io"></a><dl>

### -param <b>STORPORT_ETW_EVENT_KEYWORD_IO</b>

</dl>
</td>
<td width="60%">
<p>The event is related to device IO operations.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORPORT_ETW_EVENT_KEYWORD_PERFORMANCE"></a><a id="storport_etw_event_keyword_performance"></a><dl>

### -param <b>STORPORT_ETW_EVENT_KEYWORD_PERFORMANCE</b>

</dl>
</td>
<td width="60%">
<p>The event is performance related.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORPORT_ETW_EVENT_KEYWORD_POWER"></a><a id="storport_etw_event_keyword_power"></a><dl>

### -param <b>STORPORT_ETW_EVENT_KEYWORD_POWER</b>

</dl>
</td>
<td width="60%">
<p>The event is related to device power.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="STORPORT_ETW_EVENT_KEYWORD_ENUMERATION"></a><a id="storport_etw_event_keyword_enumeration"></a><dl>

### -param <b>STORPORT_ETW_EVENT_KEYWORD_ENUMERATION</b>

</dl>
</td>
<td width="60%">
<p>The event is related to device enumeration.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>EventLevel</i> [in]

<dd>
<p>The event level. This value can indicate the importance or severity of the event. This is one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelLogAlways"></a><a id="storportetwlevellogalways"></a><a id="STORPORTETWLEVELLOGALWAYS"></a><dl>

### -param <b>StorportEtwLevelLogAlways</b>

</dl>
</td>
<td width="60%">
<p>Log the event unconditionally. The event is logged regardless of any filters set.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelCritical"></a><a id="storportetwlevelcritical"></a><a id="STORPORTETWLEVELCRITICAL"></a><dl>

### -param <b>StorportEtwLevelCritical</b>

</dl>
</td>
<td width="60%">
<p>Critical level event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelError"></a><a id="storportetwlevelerror"></a><a id="STORPORTETWLEVELERROR"></a><dl>

### -param <b>StorportEtwLevelError</b>

</dl>
</td>
<td width="60%">
<p>Error level event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelWarning"></a><a id="storportetwlevelwarning"></a><a id="STORPORTETWLEVELWARNING"></a><dl>

### -param <b>StorportEtwLevelWarning</b>

</dl>
</td>
<td width="60%">
<p>Warning level event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelInformational"></a><a id="storportetwlevelinformational"></a><a id="STORPORTETWLEVELINFORMATIONAL"></a><dl>

### -param <b>StorportEtwLevelInformational</b>

</dl>
</td>
<td width="60%">
<p>Informational event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwLevelVerbose"></a><a id="storportetwlevelverbose"></a><a id="STORPORTETWLEVELVERBOSE"></a><dl>

### -param <b>StorportEtwLevelVerbose</b>

</dl>
</td>
<td width="60%">
<p>Verbose event information provided.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>EventOpcode</i> [in]

<dd>
<p>The operational nature of the event. This is one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeInfo"></a><a id="storportetweventopcodeinfo"></a><a id="STORPORTETWEVENTOPCODEINFO"></a><dl>

### -param <b>StorportEtwEventOpcodeInfo</b>

</dl>
</td>
<td width="60%">
<p>General informational event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeStart"></a><a id="storportetweventopcodestart"></a><a id="STORPORTETWEVENTOPCODESTART"></a><dl>

### -param <b>StorportEtwEventOpcodeStart</b>

</dl>
</td>
<td width="60%">
<p>Device or unit was starting.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeStop"></a><a id="storportetweventopcodestop"></a><a id="STORPORTETWEVENTOPCODESTOP"></a><dl>

### -param <b>StorportEtwEventOpcodeStop</b>

</dl>
</td>
<td width="60%">
<p>Device or unit was stopping. The event corresponds to the last unpaired start event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeDC_Start"></a><a id="storportetweventopcodedc_start"></a><a id="STORPORTETWEVENTOPCODEDC_START"></a><dl>

### -param <b>StorportEtwEventOpcodeDC_Start</b>

</dl>
</td>
<td width="60%">
<p>A data collection starting event. These are rundown event types.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeDC_Stop"></a><a id="storportetweventopcodedc_stop"></a><a id="STORPORTETWEVENTOPCODEDC_STOP"></a><dl>

### -param <b>StorportEtwEventOpcodeDC_Stop</b>

</dl>
</td>
<td width="60%">
<p>A data collection stopping event. These are rundown event types.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeExtension"></a><a id="storportetweventopcodeextension"></a><a id="STORPORTETWEVENTOPCODEEXTENSION"></a><dl>

### -param <b>StorportEtwEventOpcodeExtension</b>

</dl>
</td>
<td width="60%">
<p>An extension event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeReply"></a><a id="storportetweventopcodereply"></a><a id="STORPORTETWEVENTOPCODEREPLY"></a><dl>

### -param <b>StorportEtwEventOpcodeReply</b>

</dl>
</td>
<td width="60%">
<p>A reply event.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeResume"></a><a id="storportetweventopcoderesume"></a><a id="STORPORTETWEVENTOPCODERESUME"></a><dl>

### -param <b>StorportEtwEventOpcodeResume</b>

</dl>
</td>
<td width="60%">
<p>Device or unit was resuming after suspend.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeSuspend"></a><a id="storportetweventopcodesuspend"></a><a id="STORPORTETWEVENTOPCODESUSPEND"></a><dl>

### -param <b>StorportEtwEventOpcodeSuspend</b>

</dl>
</td>
<td width="60%">
<p>Device or unit is  suspended pending completion of another operation.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="StorportEtwEventOpcodeReceive"></a><a id="storportetweventopcodereceive"></a><a id="STORPORTETWEVENTOPCODERECEIVE"></a><dl>

### -param <b>StorportEtwEventOpcodeReceive</b>

</dl>
</td>
<td width="60%">
<p> Transfer of activity is received from another component.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>Srb</i> [in, optional]

<dd>
<p>A pointer to the SRB associated with the logged event. If this parameter contains a valid SRB, this SRB pointer and the associated SRB pointer are logged.</p>
</dd>

### -param <i>Parameter1Name</i> [in, optional]

<dd>
<p>A description of the of the meaning of <i>Parameter1Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.</p>
</dd>

### -param <i>Parameter1Value</i> [in]

<dd>
<p>The value for parameter 1.</p>
</dd>

### -param <i>Parameter2Name</i> [in, optional]

<dd>
<p>A description of the of the meaning of <i>Parameter2Value</i>. This parameter name string must be &lt;= STORPORT_ETW_MAX_PARAM_NAME_LENGTH.</p>
</dd>

### -param <i>Parameter2Value</i> [in]

<dd>
<p>The value for parameter 2.</p>
</dd>
</dl>

## -returns
<p><b>StorPortEtwEvent2</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The event published successfully storage ETW channel.</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>Tracing is not enabled for storage events.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>The <i>HwDeviceExtension</i> parameter is NULL.</p>

<p>-or-</p>

<p><i>EventDescription</i> is NULL.</p>

<p>-or-</p>

<p><i>EventDescription</i> is greater than the maximum name length.</p>

<p>-or-</p>

<p>An ETW parameter name is greater than the maximum name length.</p>

<p> </p>

## -remarks
<p>If any parameter is not named, ParameterXName = NULL, the routine will set the corresponding parameter value to 0.</p>

<p>Events generated from StorPort miniport drivers are published to the "Microsoft-Windows-Storage-Storport/Diagnose" ETW channel.</p>

<p>If any parameter is not named, ParameterXName = NULL, the routine will set the corresponding parameter value to 0.</p>

<p>Events generated from StorPort miniport drivers are published to the "Microsoft-Windows-Storage-Storport/Diagnose" ETW channel.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in starting with Windows 8.1.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h (include Storport.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn582029">StorPortEtwEvent4</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn582030">StorPortEtwEvent8</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20StorPortEtwEvent2 routine%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
