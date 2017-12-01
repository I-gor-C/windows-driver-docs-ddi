---
UID: NF.pepfx.PoFxRegisterPlugin
title: PoFxRegisterPlugin
author: windows-driver-content
description: The PoFxRegisterPlugin routine registers a platform extension plug-in (PEP) with the Windows power management framework (PoFx).
old-location: kernel\pofxregisterplugin.htm
old-project: kernel
ms.assetid: BB50112E-6706-419C-9686-79F0F76926C3
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PoFxRegisterPlugin
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PoFxRegisterPlugin
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
req.iface: 
---

# PoFxRegisterPlugin function



## -description
<p>The <b>PoFxRegisterPlugin</b> routine registers a platform extension plug-in (PEP) with the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx).</p>


## -syntax

````
NTSTATUS PoFxRegisterPlugin(
  _In_    PPEP_INFORMATION        PepInformation,
  _Inout_ PPEP_KERNEL_INFORMATION KernelInformation
);
````


## -parameters
<dl>

### -param <i>PepInformation</i> [in]

<dd>
<p>A pointer to a <a href="..\pepfx\ns-pepfx--pep-information.md">PEP_INFORMATION</a> structure.</p>
</dd>

### -param <i>KernelInformation</i> [in, out]

<dd>
<p>A pointer to a <a href="..\pepfx\ns-pepfx--pep-kernel-information-struct-v3.md">PEP_KERNEL_INFORMATION_STRUCT_V3</a> structure.</p>
</dd>
</dl>

## -returns
<p><b>PoFxRegisterPlugin</b> returns STATUS_SUCCESS if the call successfully registers the PEP. Possible error return values include the following status codes.</p><dl>
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

<p>The <a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a> routine is similar to <b>PoFxRegisterPlugin</b>, except that it takes an additional parameter, <i>Flags</i>.</p>

<p>The PEP must call <b>PoFxRegisterPlugin</b> at IRQL = PASSIVE_LEVEL.</p>

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
<a href="..\pepfx\ns-pepfx--pep-information.md">PEP_INFORMATION</a>
</dt>
<dt>
<a href="..\pepfx\ns-pepfx--pep-kernel-information-struct-v3.md">PEP_KERNEL_INFORMATION_STRUCT_V3</a>
</dt>
<dt>
<a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PoFxRegisterPlugin routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
