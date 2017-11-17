---
UID: NS.fwpsk.FWPS_CALLOUT1_
title: FWPS_CALLOUT1_
author: windows-driver-content
description: The FWPS_CALLOUT1 structure defines the data that is required for a callout driver to register a callout with the filter engine.Note  FWPS_CALLOUT1 is the specific version of FWPS_CALLOUT used in Windows 7 and later.
old-location: netvista\fwps_callout1.htm
ms.assetid: d15c4cd4-b4f0-4363-988a-2bbb235b7b37
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FWPS_CALLOUT1
req.alt-loc: fwpsk.h
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
ms.keywords: FWPS_CALLOUT1_, FWPS_CALLOUT1
req.iface: 
---

# FWPS_CALLOUT1_ structure



## -description
<p>The <b>FWPS_CALLOUT1</b> structure defines the data that is required for a callout driver to register a
  callout with the filter engine.</p>


## -syntax

````
typedef struct FWPS_CALLOUT1_ {
  GUID                                calloutKey;
  UINT32                              flags;
  FWPS_CALLOUT_CLASSIFY_FN1           classifyFn;
  FWPS_CALLOUT_NOTIFY_FN1             notifyFn;
  FWPS_CALLOUT_FLOW_DELETE_NOTIFY_FN0 flowDeleteFn;
} FWPS_CALLOUT1;
````


## -struct-fields
<dl>

### -field <b>calloutKey</b>

<dd>
<p>A callout driver-defined <b>GUID</b> that uniquely identifies the callout.</p>
</dd>

### -field <b>flags</b>

<dd>
<p>Flags that specify callout-specific parameters. Possible flags are:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="FWP_CALLOUT_FLAG_CONDITIONAL_ON_FLOW"></a><a id="fwp_callout_flag_conditional_on_flow"></a><dl>

### -field <b>FWP_CALLOUT_FLAG_CONDITIONAL_ON_FLOW</b>


### -field 0x00000001

</dl>
</td>
<td width="60%">
<p>A callout driver can specify this flag when registering a callout that will be added at a layer
       that supports data flows. If this flag is specified, the filter engine calls the callout driver's 
       <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a> callout function only if there
       is a context associated with the data flow. A callout driver associates a context with a data flow by
       calling the 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff551165">FwpsFlowAssociateContext0</a> function.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FWP_CALLOUT_FLAG_ALLOW_OFFLOAD"></a><a id="fwp_callout_flag_allow_offload"></a><dl>

### -field <b>FWP_CALLOUT_FLAG_ALLOW_OFFLOAD</b>


### -field 0x00000002

</dl>
</td>
<td width="60%">
<p>A callout driver specifies this flag to indicate that the callout driver's 
       <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a> callout function is unaffected
       by offloading network data processing to offload-capable network interface cards (NICs). If this flag
       is not specified, then offloading of network data processing is disabled for all traffic that is
       processed by any filters that specify the callout for the filter's action.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FWP_CALLOUT_FLAG_ENABLE_COMMIT_ADD_NOTIFY"></a><a id="fwp_callout_flag_enable_commit_add_notify"></a><dl>

### -field <b>FWP_CALLOUT_FLAG_ENABLE_COMMIT_ADD_NOTIFY</b>


### -field 0x00000004

</dl>
</td>
<td width="60%">
<p>A callout driver specifies this flag to indicate that it can receive notifications about objects and filters that are added inside a transaction. The filter engine sends the notification after the transaction is committed.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FWP_CALLOUT_FLAG_ALLOW_MID_STREAM_INSPECTION"></a><a id="fwp_callout_flag_allow_mid_stream_inspection"></a><dl>

### -field <b>FWP_CALLOUT_FLAG_ALLOW_MID_STREAM_INSPECTION</b>


### -field 0x00000008

</dl>
</td>
<td width="60%">
<p>A callout driver specifies this flag to indicate that it can perform  dynamic stream inspection of data flows at stream level. See <a href="NULL">Stream Inspection</a>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="FWP_CALLOUT_FLAG_ALLOW_RECLASSIFY"></a><a id="fwp_callout_flag_allow_reclassify"></a><dl>

### -field <b>FWP_CALLOUT_FLAG_ALLOW_RECLASSIFY</b>


### -field 0x00000010

</dl>
</td>
<td width="60%">
<p>A callout driver specifies this flag to register itself to be called when an existing socket operation is reclassified.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>classifyFn</b>

<dd>
<p>A pointer to the callout driver's 
     <a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a> callout function. The filter
     engine calls this function whenever there is network data to be processed by the callout.</p>
</dd>

### -field <b>notifyFn</b>

<dd>
<p>A pointer to the callout driver's 
     <a href="https://msdn.microsoft.com/3f377049-cc5f-427d-9b09-5e49e4b305c5">notifyFn1</a> function. The filter engine calls
     this function to notify the callout driver about events that are associated with the callout.</p>
</dd>

### -field <b>flowDeleteFn</b>

<dd>
<p>A pointer to the callout driver's 
     <a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a> callout function. The filter
     engine calls this function whenever a data flow that is being processed by the callout is terminated.
     </p>
<p>If a callout driver does not associate a context with the data flows that the callout processes, then
     this member should be set to <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>A callout driver passes a pointer to an initialized <b>FWPS_CALLOUT1</b> structure to the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a> function when it
    registers a callout with the filter engine.</p>

<p>A callout can set the <b>FWP_CALLOUT_FLAG_CONDITIONAL_ON_FLOW</b> flag only for connections on which
    the driver is interested in performing stream inspections. This callout will be ignored on all other
    connections. Performance will be improved and the driver will not have to maintain unnecessary state
    data.</p>

<p>This structure is essentially identical to the previous version, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a>. The only differences are that
    the members of this version store the updated versions of the callout function pointers, and additional flags are available for callout drivers to set.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 7.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/128fd929-6e83-46a0-9475-e459ede58f30">classifyFn1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/3f377049-cc5f-427d-9b09-5e49e4b305c5">notifyFn1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/65449a23-da5d-4884-b98e-030461eb019a">flowDeleteFn</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551224">FWPS_CALLOUT0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439700">FWPS_CALLOUT2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551143">FwpsCalloutRegister1</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FWPS_CALLOUT1 structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
