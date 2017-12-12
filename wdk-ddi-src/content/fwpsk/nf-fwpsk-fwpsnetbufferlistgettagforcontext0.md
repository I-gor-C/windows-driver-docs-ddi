---
UID: NF.fwpsk.FwpsNetBufferListGetTagForContext0
title: FwpsNetBufferListGetTagForContext0 function
author: windows-driver-content
description: The FwpsNetBufferListGetTagForContext0 function gets a locally unique context tag that can be used to associate packets with the callout driver.Note  FwpsNetBufferListGetTagForContext0 is a specific version of FwpsNetBufferListGetTagForContext.
old-location: netvista\fwpsnetbufferlistgettagforcontext0.htm
old-project: netvista
ms.assetid: f4b9b6ab-2251-4b8a-baf5-16c845a1a4db
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: FwpsNetBufferListGetTagForContext0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fwpsk.h
req.include-header: Fwpsk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with  Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FwpsNetBufferListGetTagForContext0
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

# FwpsNetBufferListGetTagForContext0 function



## -description
The <b>FwpsNetBufferListGetTagForContext0</b> function gets a locally unique context tag that can be used to
  associate packets with the callout driver.



## -syntax

````
UINT64 NTAPI FwpsNetBufferListGetTagForContext0(void);
````


## -parameters


## -returns
The 
     <b>FwpsNetBufferListGetTagForContext0</b> function returns a locally unique identifier.

The 
     <b>FwpsNetBufferListGetTagForContext0</b> function returns a locally unique identifier.

The 
     <b>FwpsNetBufferListGetTagForContext0</b> function returns a locally unique identifier.


## -remarks
The 
    <b>FwpsNetBufferListGetTagForContext0</b> function must be called before calling 
    <a href="netvista.fwpsnetbufferlistassociatecontext0">FwpsNetBufferListAssociateContext0</a>.


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
Available starting with  Windows 7.

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
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.fwpsnetbufferlistassociatecontext0">
   FwpsNetBufferListAssociateContext0</a>
</dt>
<dt>
<a href="netvista.fwpsnetbufferlistremovecontext0">
   FwpsNetBufferListRemoveContext0</a>
</dt>
<dt>
<a href="netvista.fwpsnetbufferlistretrievecontext0">
   FwpsNetBufferListRetrieveContext0</a>
</dt>
<dt>
<a href="netvista.using_packet_tagging">Using Packet Tagging</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20FwpsNetBufferListGetTagForContext0 function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

