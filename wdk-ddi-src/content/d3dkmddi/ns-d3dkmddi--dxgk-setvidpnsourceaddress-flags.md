---
UID: NS.d3dkmddi._DXGK_SETVIDPNSOURCEADDRESS_FLAGS
title: DXGK_SETVIDPNSOURCEADDRESS_FLAGS
author: windows-driver-content
description: The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's DxgkDdiSetVidPnSourceAddress or DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay functions.
old-location: display\dxgk_setvidpnsourceaddress_flags.htm
old-project: display
ms.assetid: cdc4aec6-45d4-4a5b-aa52-7830494a12b6
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_SETVIDPNSOURCEADDRESS_FLAGS, DXGK_SETVIDPNSOURCEADDRESS_FLAGS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_SETVIDPNSOURCEADDRESS_FLAGS
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

# DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure



## -description
<p>The DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure identifies the specific type of operation to perform in a call to the display miniport driver's <a href="display.dxgkddisetvidpnsourceaddress">DxgkDdiSetVidPnSourceAddress</a> or <a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a> functions.</p>


## -syntax

````
typedef struct _DXGK_SETVIDPNSOURCEADDRESS_FLAGS {
  union {
    struct {
      UINT ModeChange  :1;
      UINT FlipImmediate  :1;
      UINT FlipOnNextVSync  :1;
      UINT FlipStereo  :1;
      UINT FlipStereoTemporaryMono  :1;
      UINT FlipStereoPreferRight  :1;
      UINT SharedPrimaryTransition  :1;
      UINT IndependentFlipExclusive  :1;
      UINT MoveFlip  :1;
      UINT Reserved  :23;
    };
    UINT Value;
  };
} DXGK_SETVIDPNSOURCEADDRESS_FLAGS;
````


## -struct-fields
<dl>

### -field <b>ModeChange</b>

<dd>
<p>A UINT value that specifies for the driver to switch the display mode. </p>
<p>Setting this member is equivalent to setting the first bit of the 32-bit <b>Value</b> member (0x00000001).</p>
</dd>

### -field <b>FlipImmediate</b>

<dd>
<p>A UINT value that specifies for the driver to perform a flip operation that occurs without vertical sync.</p>
<p>Setting this member is equivalent to setting the second bit of the 32-bit <b>Value</b> member (0x00000002).</p>
</dd>

### -field <b>FlipOnNextVSync</b>

<dd>
<p>A UINT value that specifies for the driver to perform a flip operation that occurs on the next vertical sync.</p>
<p>Setting this member is equivalent to setting the third bit of the 32-bit <b>Value</b> member (0x00000004).</p>
</dd>

### -field <b>FlipStereo</b>

<dd>
<p>[in] Supported beginning with Windows 8.</p>
<p>Specifies whether the driver  flips both left and right images of a stereo allocation.</p>
<p>If the <b>FlipOnNextVSync</b> member of the <b>DXGK_SETVIDPNSOURCEADDRESS_FLAGS</b> structure is  set, the driver completes the flip to the left image on the next VSync and then completes the flip to the right image on the following VSync.</p>
<p>If the <b>FlipImmediate</b> member of the <b>DXGK_SETVIDPNSOURCEADDRESS_FLAGS</b> structure is  set, the driver immediately starts to scan out from the new allocation. For example, if the driver was scanning a right image, it  starts the new scan from the same relative offset in the right image of the new allocation.</p>
<p>The <b>FlipStereo</b> and <b>FlipStereoTemporaryMono</b> members cannot both be set at the same time.</p>
<p>For more requirements, see the Remarks section.</p>
<p>Setting this member is equivalent to setting the    fourth bit of the 32-bit <b>Value</b> member (0x00000008).</p>
</dd>

### -field <b>FlipStereoTemporaryMono</b>

<dd>
<p>[in] Supported beginning with Windows 8.</p>
<p>Specifies whether the driver uses the left image of a stereo allocation for the right and left portions of a stereo frame. The driver performs the same present operation as with <b>FlipStereo</b>, except that it scans out only from the left image to produce both images of a stereo frame.</p>
<p>This member should  be set only if the driver reports support for this option in the current display mode by setting the <b>Type</b> member of the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-vidpn-source-mode.md">D3DKMDT_VIDPN_SOURCE_MODE</a> structure to D3DKMDT_RMT_GRAPHICS_STEREO_ADVANCED_SCAN.</p>
<p>The <b>FlipStereo</b> and <b>FlipStereoTemporaryMono</b> members cannot both be set at the same time.</p>
<p>The   <b>FlipStereoTemporaryMono</b> and <b>FlipStereoPreferRight</b> members cannot both be set at the same time.</p>
<p>For more requirements, see the Remarks section.</p>
<p>Setting this member is equivalent to setting the    fifth bit of the 32-bit <b>Value</b> member (0x00000010).</p>
</dd>

### -field <b>FlipStereoPreferRight</b>

<dd>
<p>[in] Supported beginning with Windows 8.</p>
<p>Specifies that when the driver clones a stereo primary allocation to a mono monitor, it uses the right image.</p>
<p>The   <b>FlipStereoTemporaryMono</b> and <b>FlipStereoPreferRight</b> members cannot both be set at the same time.</p>
<p>For more requirements, see the Remarks section.</p>
<p>Setting this member is equivalent to setting the    sixth bit of the 32-bit <b>Value</b> member (0x00000020).</p>
</dd>

### -field <b>SharedPrimaryTransition</b>

<dd>
<p>[in] Supported beginning with Windows 8.</p>
<p>Specifies that the driver is transitioning to or from a shared managed primary allocation.</p>
<p>This member is set if either of the following transitions occurs:</p>
<ul>
<li>The current primary allocation is not a shared primary allocation, but the new one is.</li>
<li>The current primary allocation is a shared primary allocation, but the new one is not.</li>
</ul>
<p>When <b>SharedPrimaryTransition</b> is set, the display miniport driver must validate that the hardware can seamlessly switch back and forth between primary and shared primary allocations, and it must perform any hardware programming needed to make the seamless switch occur.</p>
<p>Setting this member is equivalent to setting the    seventh bit of the 32-bit <b>Value</b> member (0x00000040).</p>
</dd>

### -field <b>IndependentFlipExclusive</b>

<dd>
<p>[in] Supported beginning with Windows 10.</p>
<p>When <b>IndependentFlipExlusive</b> is set, the flip is done in the independent flip exclusive mode. The front buffer is accessed only by the display hardware (not by the DWM) and the kernel mode driver can apply vertical sync-related optimizations.   
</p>
</dd>

### -field <b>MoveFlip</b>

<dd>
<p>[in] Supported beginning with Windows 10.</p>
<p>When <b>MoveFlip</b> is set, the  driver is notified to use any state that has been saved from the previous flip to configure the new scanout request.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>[in] This member is reserved and should be set to zero. Setting this member to zero is equivalent to setting the remaining 23 bits (0xFFFFFF00) of the 32-bit <b>Value</b> member to zeros.</p>
</dd>

### -field <b>Value</b>

<dd>
<p>A member in the union that DXGK_SETVIDPNSOURCEADDRESS_FLAGS contains that can hold a 32-bit value that identifies operation type. </p>
</dd>
</dl>

## -remarks
<p>If any of the <b>FlipStereo</b>, <b>FlipStereoTemporaryMono</b>, or <b>FlipStereoPreferRight</b>  members are set, these conditions apply:</p>

<p>Beginning with Windows 8, the display miniport driver can fail a call to the <a href="display.dxgkddisetvidpnsourceaddress">DxgkDdiSetVidPnSourceAddress</a> function, returning STATUS_INVALID_PARAMETER, when the <b>SharedPrimaryTransition</b> member is set in <i>pSetVidPnSourceAddress</i>-&gt;<b>Flags</b>. However, such a failure is not expected unless there is an error in either the user mode driver's implementation of the <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-checkdirectflipsupport.md">CheckDirectFlipSupport</a> function or in the Desktop Window Manager (DWM). If such a failure occurs, the operating system will not seamlessly fail back to composition mode, and presentation will be incorrect.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows Vista.</p>
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
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-displaymode.md">D3DKMT_DISPLAYMODE</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-setvidpnsourceaddress-flags.md">DXGK_SETVIDPNSOURCEADDRESS_FLAGS</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgkarg-setvidpnsourceaddress.md">DXGKARG_SETVIDPNSOURCEADDRESS</a>
</dt>
<dt>
<a href="display.dxgkddisetvidpnsourceaddress">DxgkDdiSetVidPnSourceAddress</a>
</dt>
<dt>
<a href="display.dxgkddisetvidpnsourceaddresswithmultiplaneoverlay">DxgkDdiSetVidPnSourceAddressWithMultiPlaneOverlay</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_SETVIDPNSOURCEADDRESS_FLAGS structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
