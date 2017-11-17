---
UID: NF.fwpsk.FwpsNetBufferListRemoveContext0
title: FwpsNetBufferListRemoveContext0
author: windows-driver-content
description: The FwpsNetBufferListRemoveContext0 function removes the context associated with a network buffer list.Note  FwpsNetBufferListRemoveContext0 is a specific version of FwpsNetBufferListRemoveContext.
old-location: netvista\fwpsnetbufferlistremovecontext0.htm
ms.assetid: bd3aa1a2-3ff5-47e4-93f6-5cb2022ec630
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsNetBufferListRemoveContext0
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
ms.keywords: FwpsNetBufferListRemoveContext0
req.iface: 
---

# FwpsNetBufferListRemoveContext0 function



## -description
<p>The 
  <b>FwpsNetBufferListRemoveContext0</b> function removes the context associated with a network buffer
  list.</p>


## -syntax

````
NTSTATUS NTAPI FwpsNetBufferListRemoveContext0(
  _Inout_opt_ NET_BUFFER_LIST *netBufferList,
  _In_        UINT64          contextTag,
  _In_        UINT32          flags
);
````


## -parameters
<dl>

### -param <i>netBufferList</i> [in, out, optional]

<dd>
<p>A network buffer list that indicates one or more packets of interest to the callout driver. This
     parameter is optional and can be <b>NULL</b>. If it is <b>NULL</b>, the function will remove the context from all associated network
     buffer lists.</p>
</dd>

### -param <i>contextTag</i> [in]

<dd>
<p>The context tag that was passed in the <i>contextTag</i> parameter to 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff551191">FwpsNetBufferListAssociateContext0</a>.</p>
</dd>

### -param <i>flags</i> [in]

<dd>
<p>This parameter is reserved for future use and must be zero.</p>
</dd>
</dl>

## -returns
<p>The 
     <b>FwpsNetBufferListRemoveContext0</b> function returns one of the following <b>NTSTATUS</b> codes.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The context was successfully removed.</p><dl>
<dt><b>Other status codes</b></dt>
</dl><p>An error occurred.</p>

<p> </p>

## -remarks
<p>The 
    <b>FwpsNetBufferListRemoveContext0</b> function asynchronously removes the tagged context associated with a network buffer list.</p>

<p>To associate a context with a network buffer list, call 
    <a href="https://msdn.microsoft.com/31135396-303b-4b94-8616-a4b7be207fa1">
    FwpsNetBufferListAssociateContext0</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>.</p>

<p>Usually a callout driver will not need to use this function, because the tagged context
    is removed automatically when the packets move through the stack. This function is provided so that
    a callout driver can stop processing in situations where contexts aren't removed automatically. For example, in the case of an NDIS filter driver, the packets never enter the TCP/IP stack, and the contexts will need to be removed manually by calling <b>FwpsNetBufferListRemoveContext0</b> with the <i>netBufferList</i> parameter set to <b>NULL</b>.</p>

<p>The 
    <b>FwpsNetBufferListRemoveContext0</b> function asynchronously removes the tagged context associated with a network buffer list.</p>

<p>To associate a context with a network buffer list, call 
    <a href="https://msdn.microsoft.com/31135396-303b-4b94-8616-a4b7be207fa1">
    FwpsNetBufferListAssociateContext0</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>.</p>

<p>Usually a callout driver will not need to use this function, because the tagged context
    is removed automatically when the packets move through the stack. This function is provided so that
    a callout driver can stop processing in situations where contexts aren't removed automatically. For example, in the case of an NDIS filter driver, the packets never enter the TCP/IP stack, and the contexts will need to be removed manually by calling <b>FwpsNetBufferListRemoveContext0</b> with the <i>netBufferList</i> parameter set to <b>NULL</b>.</p>

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
<p>Available starting with  Windows 7.</p>
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
<a href="https://msdn.microsoft.com/31135396-303b-4b94-8616-a4b7be207fa1">
   FwpsNetBufferListAssociateContext0</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439674">FwpsNetBufferListAssociateContext1</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f4b9b6ab-2251-4b8a-baf5-16c845a1a4db">
   FwpsNetBufferListGetTagForContext0</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsNetBufferListRemoveContext0 function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
