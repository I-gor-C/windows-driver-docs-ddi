---
UID: NF.fwpsk.FwpsNetBufferListAssociateContext1
title: FwpsNetBufferListAssociateContext1
author: windows-driver-content
description: The FwpsNetBufferListAssociateContext1 function associates the callout driver's context with a network buffer list and configures notification for network buffer list events.Note  FwpsNetBufferListAssociateContext1 is the specific version of FwpsNetBufferListAssociateContext used in Windows 8 and later. See WFP Version-Independent Names and Targeting Specific Versions of Windows for more information. For Windows 7, FwpsNetBufferListAssociateContext0 is available.
old-location: netvista\fwpsnetbufferlistassociatecontext1.htm
ms.assetid: 86e9662e-d308-4e3a-98c1-4134186f1bad
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsNetBufferListAssociateContext1
req.alt-loc: fwpkclnt.lib,fwpkclnt.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fwpkclnt.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: FwpsNetBufferListAssociateContext1
req.iface: 
---

# FwpsNetBufferListAssociateContext1 function



## -description
<p>The 
  <b>FwpsNetBufferListAssociateContext1</b> function associates the callout driver's context with a network buffer
  list and configures notification for network buffer list events.<div class="alert"><b>Note</b>  <b>FwpsNetBufferListAssociateContext1</b> is the specific version of <b>FwpsNetBufferListAssociateContext</b> used in Windows 8 and later. See <a href="fwp.wfp_version-independent_names_and_targeting_specific_versions_of_windows">WFP Version-Independent Names and Targeting Specific Versions of Windows</a> for more information. For Windows 7, <a href="https://msdn.microsoft.com/library/windows/hardware/ff551191">FwpsNetBufferListAssociateContext0</a> is available.</div>
<div> </div>
</p>


## -syntax

````
NTSTATUS NTAPI FwpsNetBufferListAssociateContext1(
  _Inout_ NET_BUFFER_LIST                 *netBufferList,
  _In_    UINT16                          layerId,
  _In_    UINT64                          context,
  _In_    UINT64                          contextTag,
  _In_    GUID                            *providerGUID,
  _Inout_ void                            *deviceObject,
  _In_    FWPS_NET_BUFFER_LIST_NOTIFY_FN1 notifyFn,
  _In_    UINT32                          flags
);
````


## -parameters
<dl>

### -param <i>netBufferList</i> [in, out]

<dd>
<p>A network buffer list that indicates one or more packets of interest to the callout driver.</p>
</dd>

### -param <i>layerId</i> [in]

<dd>
<p>The identifier of the layer in which the context is being associated. When calling this function
     from the NDIS receive path, set this parameter to <b>FWPS_LAYER_NON_WFP</b>.</p>
</dd>

### -param <i>context</i> [in]

<dd>
<p>Arbitrary context information set by the callout driver. The filter engine will pass this context
     to the callout driver's 
     
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh451260">FWPS_NET_BUFFER_LIST_NOTIFY_FN1</a> function.</p>
</dd>

### -param <i>contextTag</i> [in]

<dd>
<p>A locally unique identifier obtained by calling the 
     <a href="https://msdn.microsoft.com/f4b9b6ab-2251-4b8a-baf5-16c845a1a4db">
     FwpsNetBufferListGetTagForContext0</a> function.</p>
</dd>

### -param <i>providerGUID</i> [in]

<dd>
<p>The provider GUID.</p>
</dd>

### -param <i>deviceObject</i> [in, out]

<dd>
<p>A pointer to the callout driver's device object.</p>
</dd>

### -param <i>notifyFn</i> [in]

<dd>
<p>A pointer to the callout driver's 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh451260">FWPS_NET_BUFFER_LIST_NOTIFY_FN1</a> function. The filter engine will send status notifications to this
     function.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>This parameter is reserved for future use and is set to zero.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsNetBufferListAssociateContext1</b> function returns one of the following NTSTATUS codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The association was successful.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>The 
    <b>FwpsNetBufferListAssociateContext1</b> function associates groups of packets with the callout driver.
    Packets of interest can be tracked for inspection through multiple layers in the stack.</p>

<p>Before calling this function, the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551192">FwpsNetBufferListGetTagForContext0</a> function must be called to obtain a context tag.</p>

<p>This function is essentially identical to the previous version, 
    
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551191">FwpsNetBufferListAssociateContext0</a>. The only difference is the 
       updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh451260">FWPS_NET_BUFFER_LIST_NOTIFY_FN1</a> function pointed to by the 
       <i>notifyFn</i> parameter.</p>

<p>The 
    <b>FwpsNetBufferListAssociateContext1</b> function associates groups of packets with the callout driver.
    Packets of interest can be tracked for inspection through multiple layers in the stack.</p>

<p>Before calling this function, the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff551192">FwpsNetBufferListGetTagForContext0</a> function must be called to obtain a context tag.</p>

<p>This function is essentially identical to the previous version, 
    
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551191">FwpsNetBufferListAssociateContext0</a>. The only difference is the 
       updated <a href="https://msdn.microsoft.com/library/windows/hardware/hh451260">FWPS_NET_BUFFER_LIST_NOTIFY_FN1</a> function pointed to by the 
       <i>notifyFn</i> parameter.</p>

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
<p>Available starting with Windows 8.</p>
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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451260">FWPS_NET_BUFFER_LIST_NOTIFY_FN1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551191">FwpsNetBufferListAssociateContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f4b9b6ab-2251-4b8a-baf5-16c845a1a4db">
   FwpsNetBufferListGetTagForContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/bd3aa1a2-3ff5-47e4-93f6-5cb2022ec630">
   FwpsNetBufferListRemoveContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/482cec75-8a21-4988-b869-639d019f9460">
   FwpsNetBufferListRetrieveContext0</a>
</dt>
<dt>
<a href="NULL">Using Packet Tagging</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsNetBufferListAssociateContext1 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
