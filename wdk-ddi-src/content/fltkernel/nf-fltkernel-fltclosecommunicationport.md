---
UID: NF.fltkernel.FltCloseCommunicationPort
title: FltCloseCommunicationPort function
author: windows-driver-content
description: FltCloseCommunicationPort closes a minifilter driver's communication server port.
old-location: ifsk\fltclosecommunicationport.htm
old-project: ifsk
ms.assetid: e3ab0d74-2c97-43da-8bee-82caa3d91c98
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltCloseCommunicationPort
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCloseCommunicationPort
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: Fltmgr.sys
req.irql: PASSIVE_LEVEL
---

# FltCloseCommunicationPort function



## -description
<b>FltCloseCommunicationPort</b> closes a minifilter driver's communication server port. 



## -syntax

````
VOID FltCloseCommunicationPort(
  _In_ PFLT_PORT ServerPort
);
````


## -parameters

### -param ServerPort [in]

Opaque port handle for the server port to be closed. This parameter is required and cannot be <b>NULL</b>. 


## -returns
None 


## -remarks
<b>FltCloseCommunicationPort</b> closes a communication server port that was created by a previous call to <a href="ifsk.fltcreatecommunicationport">FltCreateCommunicationPort</a>. 

A minifilter driver normally calls <b>FltCloseCommunicationPort</b> from its <i>FilterUnloadCallback</i> (<a href="..\fltkernel\nc-fltkernel-pflt_filter_unload_callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a>) routine. 

After <b>FltCloseCommunicationPort</b> is called, the opaque port handle specified by the <i>ServerPort</i> parameter is no longer valid and cannot safely be used. (The <i>ServerPort</i> handle is for the communication server port that the minifilter driver uses to listen for incoming connections.) 

When the communication server port is closed, existing connections are not affected. However, no more incoming connections will be accepted. 

This routine closes handle for the minifilter driver's server port, which listens for incoming connections. To disconnect a specific connection from the minifilter driver, use <a href="ifsk.fltcloseclientport">FltCloseClientPort</a>. 


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
Header

</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.filterconnectcommunicationport">FilterConnectCommunicationPort</a>
</dt>
<dt>
<a href="ifsk.fltcloseclientport">FltCloseClientPort</a>
</dt>
<dt>
<a href="ifsk.fltcreatecommunicationport">FltCreateCommunicationPort</a>
</dt>
<dt>
<a href="ifsk.fltsendmessage">FltSendMessage</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt_filter_unload_callback.md">PFLT_FILTER_UNLOAD_CALLBACK</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCloseCommunicationPort function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

