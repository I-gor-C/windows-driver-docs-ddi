---
UID: NF.wdm.ExIsProcessorFeaturePresent
title: ExIsProcessorFeaturePresent
author: windows-driver-content
description: The ExIsProcessorFeaturePresent routine queries for the existence of a specified processor feature.
old-location: kernel\exisprocessorfeaturepresent.htm
ms.assetid: d8c4d1d7-3510-48c4-b1a6-062157f4632e
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ExIsProcessorFeaturePresent
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlExPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: ExIsProcessorFeaturePresent
req.iface: 
req.product: Windows 10 or later.
---

# ExIsProcessorFeaturePresent function



## -description
<p>The <b>ExIsProcessorFeaturePresent</b> routine queries for the existence of a specified processor feature.</p>


## -syntax

````
BOOLEAN ExIsProcessorFeaturePresent(
  _In_ ULONG ProcessorFeature
);
````


## -parameters
<dl>

### -param <i>ProcessorFeature</i> [in]

<dd>
<p>Specifies one of the following constant values:</p>
<p></p>
<dl>

### -param <a id="PF_FLOATING_POINT_PRECISION_ERRATA"></a><a id="pf_floating_point_precision_errata"></a>PF_FLOATING_POINT_PRECISION_ERRATA

<dd>
<p>The processor has the Pentium floating-point divide bug.</p>
</dd>

### -param <a id="PF_FLOATING_POINT_EMULATED"></a><a id="pf_floating_point_emulated"></a>PF_FLOATING_POINT_EMULATED

<dd>
<p>The processor does not have floating-point hardware.</p>
</dd>

### -param <a id="PF_COMPARE_EXCHANGE_DOUBLE"></a><a id="pf_compare_exchange_double"></a>PF_COMPARE_EXCHANGE_DOUBLE

<dd>
<p>The processor has an 8-byte, memory-locked compare and exchange (CMPXCHG8B) instruction.</p>
</dd>

### -param <a id="PF_MMX_INSTRUCTIONS_AVAILABLE"></a><a id="pf_mmx_instructions_available"></a>PF_MMX_INSTRUCTIONS_AVAILABLE

<dd>
<p>The processor supports MMX instructions in hardware.</p>
</dd>

### -param <a id="PF_XMMI_INSTRUCTIONS_AVAILABLE"></a><a id="pf_xmmi_instructions_available"></a>PF_XMMI_INSTRUCTIONS_AVAILABLE

<dd>
<p>The processor supports SSE instructions in hardware.</p>
</dd>

### -param <a id="PF_3DNOW_INSTRUCTIONS_AVAILABLE"></a><a id="pf_3dnow_instructions_available"></a>PF_3DNOW_INSTRUCTIONS_AVAILABLE

<dd>
<p>The processor supports AMD 3DNow instructions.</p>
</dd>

### -param <a id="PF_RDTSC_INSTRUCTION_AVAILABLE"></a><a id="pf_rdtsc_instruction_available"></a>PF_RDTSC_INSTRUCTION_AVAILABLE

<dd>
<p>The processor supports a read-timestamp-counter (RDTSC) instruction.</p>
</dd>

### -param <a id="PF_PAE_ENABLED"></a><a id="pf_pae_enabled"></a>PF_PAE_ENABLED

<dd>
<p>The processor implements Physical Address Extension (PAE) support.</p>
</dd>

### -param <a id="PF_XMMI64_INSTRUCTIONS_AVAILABLE"></a><a id="pf_xmmi64_instructions_available"></a>PF_XMMI64_INSTRUCTIONS_AVAILABLE

<dd>
<p>The processor supports SSE2 instructions in hardware. This parameter value is supported only in Windows XP and later versions of Windows.</p>
</dd>

### -param <a id="PF_SSE_DAZ_MODE_AVAILABLE"></a><a id="pf_sse_daz_mode_available"></a>PF_SSE_DAZ_MODE_AVAILABLE

<dd>
<p>The processor supports the denormals-are-zero (DAZ) mode for SSE instructions. This parameter value is supported only in Windows Vista and later versions of Windows.</p>
</dd>

### -param <a id="PF_NX_ENABLED"></a><a id="pf_nx_enabled"></a>PF_NX_ENABLED

<dd>
<p><a href="http://go.microsoft.com/fwlink/p/?linkid=165498">Data execution prevention</a> is enabled. This parameter value is supported only in Windows Vista and later versions of Windows.</p>
</dd>

### -param <a id="PF_SSE3_INSTRUCTIONS_AVAILABLE"></a><a id="pf_sse3_instructions_available"></a>PF_SSE3_INSTRUCTIONS_AVAILABLE

<dd>
<p>The processor supports SSE3 instructions. This parameter value is supported only in Windows Vista and later versions of Windows.</p>
</dd>

### -param <a id="PF_COMPARE_EXCHANGE128"></a><a id="pf_compare_exchange128"></a>PF_COMPARE_EXCHANGE128

<dd>
<p>The atomic compare and exchange 128-bit operation (CMPXCHG16B) is available. This parameter value is supported only in Windows Vista and later versions of Windows.</p>
</dd>

### -param <a id="PF_COMPARE64_EXCHANGE128"></a><a id="pf_compare64_exchange128"></a>PF_COMPARE64_EXCHANGE128

<dd>
<p>The atomic compare 64-bit and exchange 128-bit operation (CMP8XCHG16) is available. This parameter value is supported only in Windows Vista and later versions of Windows.</p>
</dd>

### -param <a id="PF_XSAVE_ENABLED"></a><a id="pf_xsave_enabled"></a>PF_XSAVE_ENABLED

<dd>
<p>The processor supports the XSAVE and XRSTOR instructions. This parameter value is supported only in Windows 7 and later versions of Windows.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>ExIsProcessorFeaturePresent</b> returns <b>TRUE</b> if the specified processor feature is present; otherwise, it returns <b>FALSE</b>.</p>

## -remarks


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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
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
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547756">IrqlExPassive</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975204">PowerIrpDDis</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>