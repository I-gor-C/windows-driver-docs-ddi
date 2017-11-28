---
UID: NS.d3dkmddi._DXGK_VIDSCHCAPS
title: DXGK_VIDSCHCAPS
author: windows-driver-content
description: The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.
old-location: display\dxgk_vidschcaps.htm
old-project: display
ms.assetid: 714741b5-aec1-4d79-8199-00e8d97e6637
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_VIDSCHCAPS, DXGK_VIDSCHCAPS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available beginning with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_VIDSCHCAPS
req.alt-loc: d3dkmddi.h
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

# DXGK_VIDSCHCAPS structure



## -description
<p>The DXGK_VIDSCHCAPS structure identifies the graphics processing unit (GPU) scheduling capabilities, in bit-field flags, that a driver can support.</p>


## -syntax

````
typedef struct _DXGK_VIDSCHCAPS {
  union {
    struct {
      UINT MultiEngineAware  :1;
      UINT VSyncPowerSaveAware  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
      UINT PreemptionAware  :1;
      UINT NoDmaPatching  :1;
      UINT CancelCommandAware  :1;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
      UINT No64BitAtomics  :1;
      UINT Reserved  :26;
#else 
      UINT Reserved  :27;
#endif 
#else 
      UINT Reserved  :30;
#endif 
    };
    UINT Value;
  };
} DXGK_VIDSCHCAPS;
````


## -struct-fields
<dl>

### -field <b>MultiEngineAware</b>

<dd>
<p>A UINT value that specifies whether the driver supports the creation and destruction of a device context (through the <a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a> and <a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a> functions) and the use of a device context (through the <a href="display.dxgkddipresent">DxgkDdiPresent</a> and <a href="display.dxgkddirender">DxgkDdiRender</a> functions). If the driver does not support context creation, for every call to the driver that would pass a handle to a context, the Microsoft DirectX graphics kernel subsystem replaces the handle to the context with a handle to the device.</p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>VSyncPowerSaveAware</b>

<dd>
<p>A UINT value that specifies whether the driver supports vertical-sync power-saving functionality. 
        </p>
<p>If <b>VSyncPowerSaveAware</b> is set to 1 (<b>TRUE</b>), the operating system can save power by disabling and enabling the vertical-sync interrupt that occurs from the usage of some applications. If <b>VSyncPowerSaveAware</b> is set to zero (<b>FALSE</b>), the operating system will never disable the vertical-sync interrupt for applications that might cause the vertical-sync interrupt to occur.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
<p>Supported starting with Windows Server 2008 and Windows Vista with SP1.</p>
</dd>

### -field <b>PreemptionAware</b>

<dd>
<p>A UINT value that specifies whether the driver supports the   GPU preemption policy of Windows 8 and later versions of Windows. With this policy, the operating system always issues preemption requests to the GPU before it initiates the <a href="https://msdn.microsoft.com/f410eec7-026f-41e0-8c60-72f651659ead">Timeout Detection and Recovery
(TDR)</a> process.
        </p>
<p>If <b>PreemptionAware</b> is set to 1 (<b>TRUE</b>), the driver supports the preemption policy of Windows 8 and later versions of Windows.</p>
<p>If <b>PreemptionAware</b> is set to zero (<b>FALSE</b>), the driver supports the preemption policy  of Windows 7. With this policy, the operating system may not issue preemption requests while potentially long running operations are being executed on the GPU. As a result, these GPU requests are not preempted  before the TDR process is initiated. This may cause the TDR process to repeatedly reset the GPU which could lead to a system stop error.</p>
<div class="alert"><b>Note</b>  If <b>PreemptionAware</b> is set to 1, the <b>MultiEngineAware</b> member  must also be set to a value of 1. If <b>PreemptionAware</b> is set to 1 but <b>MultiEngineAware</b> is set to zero, the operating system will halt the driver initialization process and return a failure code.</div>
<div> </div>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>NoDmaPatching</b>

<dd>
<p>A UINT value that specifies whether the driver disables leak detection for DMA buffers that are split into multiple parts. This detection is performed after the driver's <a href="display.dxgkddipatch">DxgkDdiPatch</a> function is called to assign, or <i>patch</i>, physical addresses to each part of the DMA buffer.</p>
<div class="alert"><b>Note</b>  Display devices that support virtual addresses can reprogram a virtual address to a new video memory location without having to patch the value of the DMA buffer address. For these types of display devices, the driver should set <b>NoDmaPatching</b> to 1.</div>
<div> </div>
<p>If <b>NoDmaPatching</b> is set to 1 (<b>TRUE</b>), the driver disables leak detection, and the behavior of DMA buffer splitting is the same as in Windows 7.</p>
<p>If <b>NoDmaPatching</b> is set to 0 (<b>FALSE</b>), the driver enables leak detection for patched DMA buffer addresses. The operating system performs leak detection before it calls the driver's <a href="display.dxgkddipatch">DxgkDdiPatch</a> function.</p>
<div class="alert"><b>Note</b>  If <b>NoDmaPatching</b> is set to 1, the <b>PreemptionAware</b> and <b>MultiEngineAware</b> members  must also be set to a value of 1. If <b>NoDmaPatching</b> is set to 1 but <b>PreemptionAware</b> or <b>MultiEngineAware</b> are set to zero, the operating system will halt the driver initialization process and return a failure code.</div>
<div> </div>
<p>Setting this member is equivalent to setting the fourth bit of the 32-bit <b>Value</b> member (0x0000008).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>CancelCommandAware</b>

<dd>
<p>A UINT value that specifies whether the driver supports cleaning up internal resources (through the <a href="display.dxgkddicancelcommand">DxgkDdiCancelCommand</a> function) after a command is removed from the hardware queue.</p>
<p>If <b>CancelCommandAware</b> is set to 1 (<b>TRUE</b>), the driver supports cleaning up resources associated with a canceled DMA packet. If <b>CancelCommandAware</b> is set to zero (<b>FALSE</b>), the driver does not support cleaning up resources.</p>
<div class="alert"><b>Note</b>  If <b>CancelCommandAware</b> is set to 1, the <b>MultiEngineAware</b> member  must also be set to a value of 1. If <b>CancelCommandAware</b> is set to 1 but <b>MultiEngineAware</b> is set to zero, the operating system returns a failure code.</div>
<div> </div>
<p>Setting this member is equivalent to setting the fifth bit of the 32-bit <b>Value</b> member (0x0000010).</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>No64BitAtomics</b>

<dd>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%">
<dl>

### -field TRUE

</dl>
</td>
<td width="60%">
<p>Indicates a GPU is capable of only updating 32 bit values atomically. In this case, the OS will handle the fence wraparound case automatically, however it will place a restriction that an outstanding wait and signal fence values cannot be more than <b>UINT_MAX</b>/2 apart from the last signaled fence value.</p>
</td>
</tr>
<tr>
<td width="40%">
<dl>

### -field FALSE

</dl>
</td>
<td width="60%">
<p>Indicates a GPU is capable of updating 64 bit values atomically as visible by the CPU.</p>
</td>
</tr>
</table>
<p> </p>
<p>Supported starting with Windows 10.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>
        This member is reserved and should be set to zero.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>
        This member is reserved and should be set to zero.</p>
<p>Setting this member to zero is equivalent to setting the remaining 27 bits (0xFFFFFFE0) of the 32-bit <b>Value</b> member to zeros.</p>
<p>Supported starting with Windows 8.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero. </p>
<p>Setting this member to zero is equivalent to setting the remaining 30 bits (0xFFFFFFC) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that DXGK_VIDSCHCAPS contains that can hold a 32-bit value that identifies the GPU scheduling capabilities that the driver can support.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available beginning with Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="display.dxgkddicancelcommand">DxgkDdiCancelCommand</a>
</dt>
<dt>
<a href="display.dxgkddicreatecontext">DxgkDdiCreateContext</a>
</dt>
<dt>
<a href="display.dxgkddidestroycontext">DxgkDdiDestroyContext</a>
</dt>
<dt>
<a href="display.dxgkddipatch">DxgkDdiPatch</a>
</dt>
<dt>
<a href="display.dxgkddipresent">DxgkDdiPresent</a>
</dt>
<dt>
<a href="display.dxgkddirender">DxgkDdiRender</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_VIDSCHCAPS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
