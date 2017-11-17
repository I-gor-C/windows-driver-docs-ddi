---
UID: NC.fwpsk.FWPS_CALLOUT_NOTIFY_FN0
title: FWPS_CALLOUT_NOTIFY_FN0
author: windows-driver-content
description: The filter engine calls a callout's notifyFn0 callout function to notify the callout driver about events that are associated with the callout.Note  notifyFn0 is the specific version of notifyFn used in Windows Vista and later.
old-location: netvista\notifyfn0.htm
ms.assetid: c0f94079-7398-4998-b2b2-471aa8c538a1
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: notifyFn0
req.alt-loc: Fwpsk.h
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
ms.keywords: FwpmEngineOpen0
req.iface: 
---

# FWPS_CALLOUT_NOTIFY_FN0 callback



## -description
<p>The filter engine calls a callout's 
  <i>notifyFn0</i> callout function to notify the callout driver about events that are associated with the
  callout.</p>


## -prototype

````
FWPS_CALLOUT_NOTIFY_FN0 notifyFn0;

NTSTATUS NTAPI notifyFn0(
  _In_       FWPS_CALLOUT_NOTIFY_TYPE notifyType,
  _In_ const GUID                     *filterKey,
  _In_ const FWPS_FILTER0             *filter
)
{ ... }
````


## -parameters
<dl>

### -param <i>notifyType</i> [in]

<dd>
<p>A value that indicates the type of notification that the filter engine is sending to the callout.
     Valid values for this parameter are:
     </p>
<p></p>
<dl>

### -param <a id="FWPS_CALLOUT_NOTIFY_ADD_FILTER"></a><a id="fwps_callout_notify_add_filter"></a>FWPS_CALLOUT_NOTIFY_ADD_FILTER

<dd>
<p>A filter is being added to the filter engine that specifies the callout for the filter's
       action.</p>
</dd>

### -param <a id="FWPS_CALLOUT_NOTIFY_DELETE_FILTER"></a><a id="fwps_callout_notify_delete_filter"></a>FWPS_CALLOUT_NOTIFY_DELETE_FILTER

<dd>
<p>A filter is being deleted from the filter engine that specifies the callout for the filter's
       action.</p>
</dd>

### -param <a id="FWPS_CALLOUT_NOTIFY_TYPE_MAX"></a><a id="fwps_callout_notify_type_max"></a>FWPS_CALLOUT_NOTIFY_TYPE_MAX

<dd>
<p>A maximum value for testing purposes.</p>
</dd>
</dl>
</dd>

### -param <i>filterKey</i> [in]

<dd>
<p>A pointer to the management identifier for the filter, as specified by the application or driver
     that is adding or deleting the filter. Must be <b>NULL</b> if the 
     <i>notifyType</i> parameter is set to FWPS_CALLOUT_NOTIFY_DELETE_FILTER. For more information, see Remarks.</p>
</dd>

### -param <i>filter</i> [in]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a> structure. This structure
     describes the filter that is being added to or deleted from the filter engine.
     </p>
<p>A callout's 
     <i>notifyFn0</i> callout function can set the 
     <b>Context</b> member of this structure to point to a callout driver-supplied context structure when the
     filter is added to the filter engine. This context structure is opaque to the filter engine, and can be
     used by the callout driver's 
     <a href="https://msdn.microsoft.com/e8423c27-d3eb-4bef-a835-37fae0e2b68c">classifyFn0</a> callout function to preserve
     any driver-specific data or state information between calls by the filter engine to the callout driver's
     
     <i>classifyFn0</i> callout function.</p>
<p>A callout's 
     <i>notifyFn0</i> callout function can clean up any context associated with the filter when the filter is
     deleted from the filter engine.</p>
</dd>
</dl>

## -returns
<p>A callout's 
     <i>notifyFn0</i> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The callout driver accepts the notification from the filter engine.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred. If the 
       <i>notifyType</i> parameter is FWPS_CALLOUT_NOTIFY_ADD_FILTER, the filter will not be added to the
       filter engine. If the 
       <i>notifyType</i> parameter is FWPS_CALLOUT_NOTIFY_DELETE_FILTER, the filter will still be deleted from
       the filter engine.</p>

<p> </p>

## -remarks
<p>A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> function.</p>

<p>The filter engine calls a callout's 
    <i>notifyFn0</i> callout function to notify the callout driver about events that are associated with the
    callout. If the callout driver's 
    <i>notifyFn0</i> callout function does not recognize the type of notification that is passed in the 
    <i>notifyType</i> parameter, it ignores the notification and return STATUS_SUCCESS.</p>

<p>If a callout driver registers a callout with the filter engine after filters that specify the callout
    for the filter's action have already been added to the filter engine, the filter engine does not call the
    callout driver's 
    <i>notifyFn0</i> callout function to notify the callout about any of the existing filters. The filter
    engine calls the callout driver's 
    <i>notifyFn0</i> callout function to notify the callout when new filters that specify the callout for the
    filter's action are added to the filter engine. In this situation, a callout's 
    <i>notifyFn0</i> callout function might not get called for every filter in the filter engine that
    specifies the callout for the filter's action. If a callout driver registers a callout after the filter
    engine is started and the callout needs to know about every filter in the filter engine that specifies
    the callout for the filter's action, the callout driver must call the appropriate management functions to
    enumerate all the filters in the filter engine and sort through the resulting list of filters to find
    those that specify the callout for the filter's action. See 
    <a href="netvista.calling_other_windows_filtering_platform_functions">Calling Other
    Windows Filtering Platform Functions</a> for more information about calling these functions.</p>

<p>When a filter that specifies a callout for the filter's action is deleted from the filter engine, the
    filter engine calls the callout driver's 
    <i>notifyFn0</i> callout function and passes FWP_CALLOUT_NOTIFY_DELETE_FILTER in the 
    <i>notifyType</i> parameter and <b>NULL</b> in the 
    <i>filterKey</i> parameter. For more information, see 
    <a href="NULL">Processing Notify Callouts</a>.</p>

<p>A callout driver registers a callout's callout functions with the filter engine by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a> function.</p>

<p>The filter engine calls a callout's 
    <i>notifyFn0</i> callout function to notify the callout driver about events that are associated with the
    callout. If the callout driver's 
    <i>notifyFn0</i> callout function does not recognize the type of notification that is passed in the 
    <i>notifyType</i> parameter, it ignores the notification and return STATUS_SUCCESS.</p>

<p>If a callout driver registers a callout with the filter engine after filters that specify the callout
    for the filter's action have already been added to the filter engine, the filter engine does not call the
    callout driver's 
    <i>notifyFn0</i> callout function to notify the callout about any of the existing filters. The filter
    engine calls the callout driver's 
    <i>notifyFn0</i> callout function to notify the callout when new filters that specify the callout for the
    filter's action are added to the filter engine. In this situation, a callout's 
    <i>notifyFn0</i> callout function might not get called for every filter in the filter engine that
    specifies the callout for the filter's action. If a callout driver registers a callout after the filter
    engine is started and the callout needs to know about every filter in the filter engine that specifies
    the callout for the filter's action, the callout driver must call the appropriate management functions to
    enumerate all the filters in the filter engine and sort through the resulting list of filters to find
    those that specify the callout for the filter's action. See 
    <a href="netvista.calling_other_windows_filtering_platform_functions">Calling Other
    Windows Filtering Platform Functions</a> for more information about calling these functions.</p>

<p>When a filter that specifies a callout for the filter's action is deleted from the filter engine, the
    filter engine calls the callout driver's 
    <i>notifyFn0</i> callout function and passes FWP_CALLOUT_NOTIFY_DELETE_FILTER in the 
    <i>notifyType</i> parameter and <b>NULL</b> in the 
    <i>filterKey</i> parameter. For more information, see 
    <a href="NULL">Processing Notify Callouts</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552387">FWPS_FILTER0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551140">FwpsCalloutRegister0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568802">notifyFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f377049-cc5f-427d-9b09-5e49e4b305c5">notifyFn1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c70c987b-5b4c-4ddd-8eb8-8c3c40003ab3">notifyFn2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543875">Callout Driver Callout Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT_NOTIFY_FN0 callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
