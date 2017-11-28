---
UID: NF.mrx.__RxFillAndInstallFastIoDispatch
title: __RxFillAndInstallFastIoDispatch
author: windows-driver-content
description: RxFillAndInstallFastIoDispatch fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed.
old-location: ifsk\__rxfillandinstallfastiodispatch.htm
old-project: ifsk
ms.assetid: 4619a1aa-0c91-4b77-abbf-077f28437e0f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: __RxFillAndInstallFastIoDispatch
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
req.alt-api: __RxFillAndInstallFastIoDispatch
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

# __RxFillAndInstallFastIoDispatch function



## -description
<p><b>RxFillAndInstallFastIoDispatch</b> fills out a fast I/O dispatch vector to be identical with the normal dispatch I/O vector and installs it into the driver object associated with the device object passed.</p>


## -syntax

````
VOID __RxFillAndInstallFastIoDispatch(
  _In_    PRDBSS_DEVICE_OBJECT RxDeviceObject,
  _Inout_ PFAST_IO_DISPATCH    FastIoDispatch,
  _In_    ULONG                FastIoDispatchSize
);
````


## -parameters
<dl>

### -param <i>RxDeviceObject</i> [in]

<dd>
<p>A pointer to the RDBSS device object for this network redirector.</p>
</dd>

### -param <i>FastIoDispatch</i> [in, out]

<dd>
<p>A pointer to the fast I/O dispatch table to fill in and use.</p>
</dd>

### -param <i>FastIoDispatchSize</i> [in]

<dd>
<p>The size, in bytes, of the fast I/O dispatch table passed.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>__RxFillAndInstallFastIoDispatch</b> routine is implemented differently for monolithic and non-monolithic drivers network mini-redirector. </p>

<p>For non-monolithic network mini-redirector drivers, such as the Microsoft SMB redirector that links to rdbss.sys dynamically, <b>__RxFillAndInstallFastIoDispatch</b> is a convenience routine that copies the normal dispatch I/O vector table routines to the fast I/O dispatch vector table. This routine would normally be used by a non-monolithic network mini-redirector to fill out the fast I/O dispatch table before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554693">RxRegisterMiniRdr</a>. This routine uses the minimum of the <i>FastIoDispatchSize</i> parameter and the size of the FAST_IO_DISPATCH structure defined in ntifs.h to determine the number of bytes to copy.</p>

<p>For monolithic network mini-redirectors built by developers, the <b>__RxFillAndInstallFastIoDispatch</b> routine does nothing.</p>

<p>The <b>__RxFillAndInstallFastIoDispatch</b> routine is implemented differently for monolithic and non-monolithic drivers network mini-redirector. </p>

<p>For non-monolithic network mini-redirector drivers, such as the Microsoft SMB redirector that links to rdbss.sys dynamically, <b>__RxFillAndInstallFastIoDispatch</b> is a convenience routine that copies the normal dispatch I/O vector table routines to the fast I/O dispatch vector table. This routine would normally be used by a non-monolithic network mini-redirector to fill out the fast I/O dispatch table before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff554693">RxRegisterMiniRdr</a>. This routine uses the minimum of the <i>FastIoDispatchSize</i> parameter and the size of the FAST_IO_DISPATCH structure defined in ntifs.h to determine the number of bytes to copy.</p>

<p>For monolithic network mini-redirectors built by developers, the <b>__RxFillAndInstallFastIoDispatch</b> routine does nothing.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554693">RxRegisterMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554718">RxSetDomainForMailslotBroadcast</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554736">RxStartMiniRdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554743">RxStopMiniRdr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20__RxFillAndInstallFastIoDispatch function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
