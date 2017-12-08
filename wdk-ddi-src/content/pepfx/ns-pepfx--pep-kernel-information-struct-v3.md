---
UID: NS.pepfx._PEP_KERNEL_INFORMATION_STRUCT_V3
title: PEP_KERNEL_INFORMATION_STRUCT_V3
author: windows-driver-content
description: The PEP_KERNEL_INFORMATION_STRUCT_V3 structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows power management framework (PoFx).
old-location: kernel\pep_kernel_information_struct_v3.htm
old-project: kernel
ms.assetid: AA3E273F-FCC0-4633-8A4C-194DA1C0E0D7
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PEP_KERNEL_INFORMATION_STRUCT_V3, PEP_KERNEL_INFORMATION_STRUCT_V3, *PPEP_KERNEL_INFORMATION_STRUCT_V3
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_KERNEL_INFORMATION_STRUCT_V3
req.alt-loc: pepfx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PEP_KERNEL_INFORMATION_STRUCT_V3 structure



## -description
<p>The <b>PEP_KERNEL_INFORMATION_STRUCT_V3</b> structure specifies the interface that the power extension plug-in (PEP) uses to request services from the Windows <a href="kernel.power_management_framework__pofx__routines">power management framework</a> (PoFx).</p>


## -syntax

````
typedef struct _PEP_KERNEL_INFORMATION_STRUCT_V3 {
  USHORT                                   Version;
  USHORT                                   Size;
  POHANDLE                                 Plugin;
  PPOFXCALLBACKREQUESTWORKER               RequestWorker;
  PPOFXCALLBACKENUMERATEUNMASKEDINTERRUPTS EnumerateUnmaskedInterrupts;
  PPOFXCALLBACKPROCESSORHALT               ProcessorHalt;
  PPOFXCALLBACKREQUESTINTERRUPT            RequestInterrupt;
  PPOFXCALLBACKCRITICALRESOURCE            TransitionCriticalResource;
  PPOFXCALLBACKPROCESSORIDLEVETO           ProcessorIdleVeto;
  PPOFXCALLBACKPLATFORMIDLEVETO            PlatformIdleVeto;
  PPOFXCALLBACKUPDATEPROCESSORIDLESTATE    UpdateProcessorIdleState;
  PPOFXCALLBACKUPDATEPLATFORMIDLESTATE     UpdatePlatformIdleState;
  PPOFXCALLBACKREQUESTCOMMON               RequestCommon;
} PEP_KERNEL_INFORMATION_STRUCT_V3, *PPEP_KERNEL_INFORMATION_STRUCT_V3;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>The current version number for this structure. Set this member to <b>PEP_KERNEL_INFORMATION_VERSION</b>.</p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of this structure. Set this member to <b>sizeof</b>(<b>PEP_KERNEL_INFORMATION</b>).</p>
</dd>

### -field Plugin

<dd>
<p>The handle assigned to the PEP's registration with PoFx. PoFx sets the value of this member. The PEP uses this handle in calls to the <a href="kernel.requestworker">RequestWorker</a> routine.</p>
</dd>

### -field RequestWorker

<dd>
<p>A pointer to a <a href="kernel.requestworker">RequestWorker</a> routine. PoFx sets the value of this member. The <b>RequestWorker</b> routine is implemented by PoFx. The PEP calls this routine to request the use of a worker thread from the operating system.</p>
</dd>

### -field EnumerateUnmaskedInterrupts

<dd>
<p>A pointer to an <a href="kernel.enumerateunmaskedinterrupts">EnumerateUnmaskedInterrupts</a> routine. PoFx sets the value of this member. The <b>EnumerateUnmaskedInterrupts</b> routine is implemented by PoFx. The PEP calls this routine to request information about the unmasked interrupts.</p>
</dd>

### -field ProcessorHalt

<dd>
<p>A pointer to a <a href="kernel.processorhalt">ProcessorHalt</a> routine. PoFx sets the value of this member. The <b>ProcessorHalt</b> routine is implemented by PoFx. The PEP calls this routine to prepare the current processor to enter the halted state.</p>
</dd>

### -field RequestInterrupt

<dd>
<p>A pointer to a <a href="kernel.requestinterrupt">RequestInterrupt</a> routine. PoFx sets the value of this member. The <b>RequestInterrupt</b> routine is implemented by PoFx. The PEP calls this routine to replay an edge-triggered interrupt that might have been lost after the hardware platform entered a low-power system state.</p>
</dd>

### -field TransitionCriticalResource

<dd>
<p>A pointer to a <a href="kernel.transitioncriticalresource">TransitionCriticalResource</a> routine. PoFx sets the value of this member. The <b>TransitionCriticalResource</b> routine is implemented by PoFx. The PEP calls this routine to transition critical system resources to the idle condition.</p>
</dd>

### -field ProcessorIdleVeto

<dd>
<p>A pointer to a <a href="kernel.processoridleveto">ProcessorIdleVeto</a> routine. PoFx sets the value of this member. The <b>ProcessorIdleVeto</b> routine is implemented by PoFx. The PEP calls this routine to increment or decrement the veto count for a pending transition to a processor idle state.</p>
</dd>

### -field PlatformIdleVeto

<dd>
<p>A pointer to a <a href="kernel.platformidleveto">PlatformIdleVeto</a> routine. PoFx sets the value of this member. The <b>PlatformIdleVeto</b> routine is implemented by PoFx. The PEP calls this routine to increment or decrement the veto count for a pending transition to a platform idle state.</p>
</dd>

### -field UpdateProcessorIdleState

<dd>
<p>A pointer to an <a href="kernel.updateprocessoridlestate">UpdateProcessorIdleState</a> routine. PoFx sets the value of this member. The <b>UpdateProcessorIdleState</b> routine is implemented by PoFx. The PEP calls this routine to update the properties of the specified processor idle state.</p>
</dd>

### -field UpdatePlatformIdleState

<dd>
<p>A pointer to an <a href="kernel.updateplatformidlestate">UpdatePlatformIdleState</a> routine. PoFx sets the value of this member. The <b>UpdatePlatformIdleState</b> routine is implemented by PoFx. The PEP calls this routine to update the properties of the specified platform idle state.</p>
</dd>

### -field RequestCommon

<dd>
<p>A pointer to an <a href="..\pepfx\nc-pepfx-pofxcallbackrequestcommon.md">RequestCommon</a> routine. PoFx sets the value of this member. The <b>RequestCommon</b> routine is implemented by PoFx. The PEP calls this routine to perform a processing operation that is specified by a request ID.</p>
</dd>
</dl>

## -remarks
<p>The <b>KernelInformation</b> parameter to the <a href="..\pepfx\nf-pepfx-pofxregisterplugin.md">PoFxRegisterPlugin</a> or <a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a> routine is a pointer to a <b>PEP_KERNEL_INFORMATION</b> structure. The PEP allocates this structure and sets the values of the <b>Version</b> and <b>Size</b> members of this structure before calling <b>PoFxRegisterPlugin</b> or <b>PoFxRegisterPluginEx</b>. During the call to this routine, PoFx fills in the remaining members of the structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 10.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="kernel.enumerateunmaskedinterrupts">EnumerateUnmaskedInterrupts</a>
</dt>
<dt>
<a href="kernel.platformidleveto">PlatformIdleVeto</a>
</dt>
<dt>
<a href="..\pepfx\nf-pepfx-pofxregisterplugin.md">PoFxRegisterPlugin</a>
</dt>
<dt>
<a href="..\pepfx\nf-pepfx-pofxregisterpluginex.md">PoFxRegisterPluginEx</a>
</dt>
<dt>
<a href="kernel.processorhalt">ProcessorHalt</a>
</dt>
<dt>
<a href="kernel.processoridleveto">ProcessorIdleVeto</a>
</dt>
<dt>
<a href="..\pepfx\nc-pepfx-pofxcallbackrequestcommon.md">RequestCommon</a>
</dt>
<dt>
<a href="kernel.requestinterrupt">RequestInterrupt</a>
</dt>
<dt>
<a href="kernel.requestworker">RequestWorker</a>
</dt>
<dt>
<a href="kernel.transitioncriticalresource">TransitionCriticalResource</a>
</dt>
<dt>
<a href="kernel.updateplatformidlestate">UpdatePlatformIdleState</a>
</dt>
<dt>
<a href="kernel.updateprocessoridlestate">UpdateProcessorIdleState</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_KERNEL_INFORMATION_STRUCT_V3 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
