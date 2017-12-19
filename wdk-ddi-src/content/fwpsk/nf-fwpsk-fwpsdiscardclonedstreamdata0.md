---
UID: NF.fwpsk.FwpsDiscardClonedStreamData0
title: FwpsDiscardClonedStreamData0 function
author: windows-driver-content
description: The FwpsDiscardClonedStreamData0 function frees the memory buffer that is allocated by the FwpsCloneStreamData0 function.Note  FwpsDiscardClonedStreamData0 is a specific version of FwpsDiscardClonedStreamData.
old-location: netvista\fwpsdiscardclonedstreamdata0.htm
old-project: NetVista
ms.assetid: 11e8338d-4ca3-49a4-8cfe-ac9f15434b4f
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: FwpsDiscardClonedStreamData0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsDiscardClonedStreamData0
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
---

# FwpsDiscardClonedStreamData0 function



## -description
The 
  <b>FwpsDiscardClonedStreamData0</b> function frees the memory buffer that is allocated by the 
  <a href="netvista.fwpsclonestreamdata0">FwpsCloneStreamData0</a> function.



## -syntax

````
void NTAPI FwpsDiscardClonedStreamData0(
  _Inout_ NET_BUFFER_LIST *netBufferListChain,
  _In_    UINT32          flags,
  _In_    BOOLEAN         dispatchLevel
);
````


## -parameters

### -param netBufferListChain [in, out]

A pointer to the 
     <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure chain that is
     being freed. This will be the same as the 
     <i>netBufferListChain</i> parameter of the 
     <a href="netvista.fwpsclonestreamdata0">FwpsCloneStreamData0</a> function.


### -param flags [in]

There are currently no flags defined for this function. Callout drivers should set this parameter
     to zero.


### -param dispatchLevel [in]

A value that indicates the current IRQL = DISPATCH_LEVEL. A callout driver should set this
     parameter to <b>TRUE</b> only if it is running at IRQL = DISPATCH_LEVEL. Otherwise, a callout driver should set
     this parameter to <b>FALSE</b>.


## -returns
None.


## -remarks
This function can be called when a cloned 
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> chain is to be discarded
    instead of being reinjected back into the data stream.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows Vista.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Fwpsk.h (include Fwpsk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Fwpkclnt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.fwpsclonestreamdata0">FwpsCloneStreamData0</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20FwpsDiscardClonedStreamData0 function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

