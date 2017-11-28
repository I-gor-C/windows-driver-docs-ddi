---
UID: NF.wdm.IoGetRemainingStackSize
title: IoGetRemainingStackSize
author: windows-driver-content
description: The IoGetRemainingStackSize routine returns the current amount of available kernel-mode stack space.
old-location: kernel\iogetremainingstacksize.htm
old-project: kernel
ms.assetid: 5e257b72-fe16-49a0-9232-9c791a88e903
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IoGetRemainingStackSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoGetRemainingStackSize
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section.
req.iface: 
req.product: Windows 10 or later.
---

# IoGetRemainingStackSize function



## -description
<p>The <b>IoGetRemainingStackSize</b> routine returns the current amount of available kernel-mode stack space.</p>


## -syntax

````
ULONG_PTR IoGetRemainingStackSize(void);
````


## -parameters


## -returns
<p><b>IoGetRemainingStackSize</b> returns the number of bytes of stack space in the current thread context.</p>

<p><b>IoGetRemainingStackSize</b> returns the number of bytes of stack space in the current thread context.</p>

<p><b>IoGetRemainingStackSize</b> returns the number of bytes of stack space in the current thread context.</p>

## -remarks
<p>Highest-level drivers, such as file systems, can call this routine, particularly drivers that use recursive code paths. Such a driver would call <b>IoGetRemainingStackSize</b> before launching a recursion to determine whether it should continue processing on an alternate code path.</p>

<p>For Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows, callers of <b>IoGetRemainingStackSize</b> can be running at any IRQL. For earlier versions of Windows, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

<p>Highest-level drivers, such as file systems, can call this routine, particularly drivers that use recursive code paths. Such a driver would call <b>IoGetRemainingStackSize</b> before launching a recursion to determine whether it should continue processing on an alternate code path.</p>

<p>For Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows, callers of <b>IoGetRemainingStackSize</b> can be running at any IRQL. For earlier versions of Windows, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

<p>Highest-level drivers, such as file systems, can call this routine, particularly drivers that use recursive code paths. Such a driver would call <b>IoGetRemainingStackSize</b> before launching a recursion to determine whether it should continue processing on an alternate code path.</p>

<p>For Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows, callers of <b>IoGetRemainingStackSize</b> can be running at any IRQL. For earlier versions of Windows, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

<p>Highest-level drivers, such as file systems, can call this routine, particularly drivers that use recursive code paths. Such a driver would call <b>IoGetRemainingStackSize</b> before launching a recursion to determine whether it should continue processing on an alternate code path.</p>

<p>For Windows Server 2003 Service Pack 1 (SP1) and later versions of Windows, callers of <b>IoGetRemainingStackSize</b> can be running at any IRQL. For earlier versions of Windows, the caller must be running at IRQL &lt;= APC_LEVEL.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>See Remarks section.</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549247">IoGetInitialStack</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549299">IoGetStackLimits</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoGetRemainingStackSize routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
