---
UID: NF.mrx.RxSetDomainForMailslotBroadcast
title: RxSetDomainForMailslotBroadcast
author: windows-driver-content
description: RxSetDomainForMailslotBroadcast is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver.
old-location: ifsk\rxsetdomainformailslotbroadcast.htm
old-project: ifsk
ms.assetid: 22f5e525-bdf8-4047-9b77-6523cb59f090
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RxSetDomainForMailslotBroadcast
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxSetDomainForMailslotBroadcast
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# RxSetDomainForMailslotBroadcast function



## -description
<p><b>RxSetDomainForMailslotBroadcast</b> is called by a network mini-redirector driver to set the domain used for mailslot broadcasts if mailslots are supported by the driver. </p>


## -syntax

````
NTSTATUS RxSetDomainForMailslotBroadcast(
  _In_ PUNICODE_STRING DomainName
);
````


## -parameters
<dl>

### -param DomainName [in]

<dd>
<p>A pointer to a buffer that contains a zero-terminated Unicode string that names the domain to use for mailslots. </p>
</dd>
</dl>

## -returns
<p><b>RxSetDomainForMailslotBroadcast</b> returns STATUS_SUCCESS on success or one of the following error values on failure: </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There were insufficient resources to complete this routine. The memory allocation request failed for nonpaged pool memory to store the domain name.</p>

<p> </p>

## -remarks
<p>A network mini-redirector registers with RDBSS whenever the driver is loaded by the kernel and unregisters with RDBSS when the driver is unloaded. This registration process is a two-way hand shake in which the network mini-redirector informs RDBSS that it has been loaded by calling <b>RxRegisterMinirdr</b>, the registration routine exported from RDBSS. RDBSS completes the registration and initialization process by calling <b>MrxStart</b>, one of the callback routines exported by the network mini-redirector and passed in as part of the dispatch table to <b>RxRegisterMinirdr</b>.</p>

<p>One of the parameters passed to the <b>RxRegisterMinirdr</b> routine indicates whether the network mini-redirector supports mailslots. A network mini-redirector would normally call <b>RxSetDomainForMailslotBroadcast</b> from the <b>MrxStart</b> routine or as part of an external request to start the driver initiated by a file system control (FSCTRL) or an I/O control (IOCTL) request from a user-mode application or service.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mrx.h (include Mrx.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-iocreatedevice.md">IoCreateDevice</a>
</dt>
<dt>
<a href="..\mrx\nf-mrx-rxregisterminirdr.md">RxRegisterMinirdr</a>
</dt>
<dt>
<a href="..\mrx\nf-mrx-rxstartminirdr.md">RxStartMinirdr</a>
</dt>
<dt>
<a href="..\mrx\nf-mrx-rxstopminirdr.md">RxStopMinirdr</a>
</dt>
<dt>
<a href="..\mrx\nf-mrx---rxfillandinstallfastiodispatch.md">__RxFillAndInstallFastIoDispatch</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxSetDomainForMailslotBroadcast function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
