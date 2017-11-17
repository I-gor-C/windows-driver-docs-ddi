---
UID: NF.pepfx.PoFxRegisterPluginEx
title: PoFxRegisterPluginEx
author: windows-driver-content
description: The PoFxRegisterPluginEx routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx).
old-location: kernel\pofxregisterpluginex.htm
ms.assetid: 68753690-A6DC-46BE-9981-F395B98C3245
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxRegisterPluginEx
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: PoFxRegisterPluginEx
req.iface: 
---

# PoFxRegisterPluginEx function



## -description
<p>The <b>PoFxRegisterPluginEx</b> routine registers a platform extension plug-in (PEP) with the Windows <a href="https://msdn.microsoft.com/B08F8ABF-FD43-434C-A345-337FBB799D9B">power management framework</a> (PoFx).</p>


## -syntax

````
NTSTATUS PoFxRegisterPluginEx(
  _In_    PPEP_INFORMATION        PepInformation,
  _In_    ULONGLONG               Flags,
  _Inout_ PPEP_KERNEL_INFORMATION KernelInformation
);
````


## -parameters
<dl>

### -param <i>PepInformation</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt186745">PEP_INFORMATION</a> structure that contains pointers to one or more callback routines that are implemented by the PEP. These routines handle notifications that are sent to the PEP by PoFx.</p>
</dd>

### -param <i>Flags</i> [in]

<dd>
<p>A set of flag bits for configuring the PEP interface. Set this member to zero or to the following value.</p>
<table>
<tr>
<th>Flag bit</th>
<th>Description</th>
</tr>
<tr>
<td>PEP_FLAG_WORKER_CONCURRENCY</td>
<td></td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>KernelInformation</i> [in, out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/mt629114">PEP_KERNEL_INFORMATION</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>PoFxRegisterPluginEx</b> returns STATUS_SUCCESS if the call successfully registers the PEP. Possible error return values include the following status codes.</p><dl>
<dt>STATUS_INVALID_PARAMETER</dt>
</dl><p>The <b>Version</b> or <b>Size</b> member of the <b>PEP_KERNEL_INFORMATION</b> structure is set to an invalid value; or the <b>AcceptDeviceNotification</b> member of this structure is set to NULL.</p><dl>
<dt>STATUS_INVALID_PEP_INFO_VERSION</dt>
</dl><p>The <b>Version</b> member of the <b>PEP_INFORMATION</b> structure is set to an invalid value.</p><dl>
<dt>STATUS_INSUFFICIENT_RESOURCES</dt>
</dl><p>Unable to allocate the resources required to complete the requested registration.</p>

<p> </p>

## -remarks
<p>A PEP calls this routine to register itself with PoFx.</p>

<p>A PEP cannot unregister, and cannot register twice. If the PEP must be serviced, the operating system must restart.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt186873">PoFxRegisterPlugin</a> routine is similar to <b>PoFxRegisterPluginEx</b>, except that it does not take a <i>Flags</i> parameter.</p>

<p>The PEP must call <b>PoFxRegisterPluginEx</b> at IRQL = PASSIVE_LEVEL.</p>

<p>A PEP calls this routine to register itself with PoFx.</p>

<p>A PEP cannot unregister, and cannot register twice. If the PEP must be serviced, the operating system must restart.</p>

<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/mt186873">PoFxRegisterPlugin</a> routine is similar to <b>PoFxRegisterPluginEx</b>, except that it does not take a <i>Flags</i> parameter.</p>

<p>The PEP must call <b>PoFxRegisterPluginEx</b> at IRQL = PASSIVE_LEVEL.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ntoskrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186745">PEP_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt629114">PEP_KERNEL_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186873">PoFxRegisterPlugin</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxRegisterPluginEx routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
