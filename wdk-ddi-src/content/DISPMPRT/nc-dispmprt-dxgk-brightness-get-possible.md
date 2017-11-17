---
UID: NC.dispmprt.DXGK_BRIGHTNESS_GET_POSSIBLE
title: DXGK_BRIGHTNESS_GET_POSSIBLE
author: windows-driver-content
description: The DxgkDdiGetPossibleBrightness function retrieves the brightness levels that an integrated display panel supports.
old-location: display\dxgkddigetpossiblebrightness.htm
ms.assetid: aed565f5-a9c1-4130-a192-68bb699b4bd1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: dispmprt.h
req.include-header: Dispmprt.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DxgkDdiGetPossibleBrightness
req.alt-loc: dispmprt.h
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
ms.keywords: SYMBOL_INFO_EX, SYMBOL_INFO_EX, *PSYMBOL_INFO_EX
req.iface: IDebugSystemObjects4
---

# DXGK_BRIGHTNESS_GET_POSSIBLE callback



## -description
<p>The <i>DxgkDdiGetPossibleBrightness</i> function retrieves the brightness levels that an integrated display panel supports.</p>


## -prototype

````
DXGK_BRIGHTNESS_GET_POSSIBLE DxgkDdiGetPossibleBrightness;

NTSTATUS* DxgkDdiGetPossibleBrightness(
  _In_  PVOID  Context,
  _In_  ULONG  BufferSize,
  _Out_ PUCHAR LevelCount,
  _Out_ PUCHAR BrightnessLevels
)
{ ... }
````


## -parameters
<dl>

### -param <i>Context</i> [in]

<dd>
<p>[in] A handle to a context block that is associated with a display adapter. The display miniport driver's <a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a> function previously provided this handle to the Microsoft DirectX graphics kernel subsystem.</p>
</dd>

### -param <i>BufferSize</i> [in]

<dd>
<p>[in] The size, in bytes, of the buffer that is passed in the <i>BrightnessLevels</i> parameter. </p>
</dd>

### -param <i>LevelCount</i> [out]

<dd>
<p>[out] A pointer to a variable that receives the number of brightness levels that the driver returns in the buffer that the <i>BrightnessLevels</i> parameter points to. </p>
</dd>

### -param <i>BrightnessLevels</i> [out]

<dd>
<p>[in/out] A pointer to a buffer that receives the brightness levels that an integrated display panel supports.</p>
</dd>
</dl>

## -returns
<p><i>DxgkDdiGetPossibleBrightness</i> returns STATUS_SUCCESS if it succeeds. Otherwise, it returns one of the error codes that are defined in <i>Ntstatus.h</i>. </p>

## -remarks
<p>The display miniport driver should return brightness levels in the buffer that the <i>BrightnessLevels</i> parameter points to in the following order:</p>

<p>The first brightness level value is the brightness level that the BIOS uses when the computer runs on AC power. </p>

<p>The second brightness level value is the brightness level that the BIOS uses when the computer runs on DC power. </p>

<p>The remaining brightness level values are hardware-supported brightness levels. </p>

<p>To simplify your job of implementing a display miniport driver, the operating system provides the driver with the buffer that the <i>BrightnessLevels</i> parameter points to.</p>

<p><i>DxgkDdiGetPossibleBrightness</i> should be made pageable. </p>

<p>The display miniport driver should return brightness levels in the buffer that the <i>BrightnessLevels</i> parameter points to in the following order:</p>

<p>The first brightness level value is the brightness level that the BIOS uses when the computer runs on AC power. </p>

<p>The second brightness level value is the brightness level that the BIOS uses when the computer runs on DC power. </p>

<p>The remaining brightness level values are hardware-supported brightness levels. </p>

<p>To simplify your job of implementing a display miniport driver, the operating system provides the driver with the buffer that the <i>BrightnessLevels</i> parameter points to.</p>

<p><i>DxgkDdiGetPossibleBrightness</i> should be made pageable. </p>

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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dispmprt.h (include Dispmprt.h)</dt>
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
<a href="https://msdn.microsoft.com/5fd4046f-54c3-4dfc-8d51-0d9ebcde0bea">DxgkDdiAddDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_BRIGHTNESS_GET_POSSIBLE callback function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
