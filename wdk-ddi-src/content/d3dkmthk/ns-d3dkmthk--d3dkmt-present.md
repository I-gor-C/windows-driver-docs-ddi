---
UID: NS.d3dkmthk._D3DKMT_PRESENT
title: D3DKMT_PRESENT
author: windows-driver-content
description: The D3DKMT_PRESENT structure describes the present operation.
old-location: display\d3dkmt_present.htm
old-project: display
ms.assetid: 959d17f1-588b-4b65-a3ea-e4609aa84eed
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT, D3DKMT_PRESENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PRESENT
req.alt-loc: d3dkmthk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# D3DKMT_PRESENT structure



## -description
<p>The D3DKMT_PRESENT structure describes the present operation.</p>


## -syntax

````
typedef struct _D3DKMT_PRESENT {
  union {
    D3DKMT_HANDLE hDevice;
    D3DKMT_HANDLE hContext;
  };
  HWND                           hWindow;
  D3DDDI_VIDEO_PRESENT_SOURCE_ID VidPnSourceId;
  D3DKMT_HANDLE                  hSource;
  D3DKMT_HANDLE                  hDestination;
  UINT                           Color;
  RECT                           DstRect;
  RECT                           SrcRect;
  UINT                           SubRectCnt;
  const RECT                     *pSrcSubRects;
  UINT                           PresentCount;
  D3DDDI_FLIPINTERVAL_TYPE       FlipInterval;
  D3DKMT_PRESENTFLAGS            Flags;
  ULONG                          BroadcastContextCount;
  D3DKMT_HANDLE                  BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  HANDLE                         PresentLimitSemaphore;
  D3DKMT_PRESENTHISTORYTOKEN     PresentHistoryToken;
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WIN8)
  D3DKMT_PRESENT_RGNS            *pPresentRegions;
#endif 
} D3DKMT_PRESENT;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device to present to. A device handle is supplied to the <a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtpresent.md">D3DKMTPresent</a> function in the union that D3DKMT_PRESENT contains for compatibility with Microsoft Direct3D version 10.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the device context to present to.</p>
</dd>

### -field <b>hWindow</b>

<dd>
<p>[in] A handle to the window that the bit-block transfer (bitblt) applies to. A value of <b>NULL</b> indicates the desktop window. The value in <b>hWindow</b> can be <b>NULL</b> unless the <b>Blt</b> or <b>ColorFill</b> bit-field flag is specified in the <b>Flags</b> member. </p>
</dd>

### -field <b>VidPnSourceId</b>

<dd>
<p>[in] The zero-based identification number of the video present source in a path of a video present network (VidPN) topology on which to restrict displaying, if the <b>RestrictVidPnSource</b> bit-field flag is set in the <b>Flags</b> member.</p>
<p>If the <b>RestrictVidPnSource</b> bit-field flag is set and the <b>hWindow</b> member is <b>NULL</b>, the <b>VidPnSourceId</b> member indicates which output the full-screen bitblt is directed to If <b>RestrictVidPnSource</b> is set and <b>hWindow</b> is non-<b>NULL</b>, <b>VidPnSourceId</b> indicates to which output to restrict the windowed bit-block transfer. </p>
</dd>

### -field <b>hSource</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the system memory or primary allocation to present from, if the <b>ColorFill</b> bit-field flag is not set in the <b>Flags</b> member.</p>
</dd>

### -field <b>hDestination</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the destination allocation. <b>hDestination</b> can be zero if the destination is unknown. </p>
<p>The handle in <b>hDestination</b> is valid only if the <b>Blt</b> bit-field flag is set in the <b>Flags</b> member.</p>
<p>If the handle in the <b>hDestination</b> member is nonzero, the <b>hDestination</b> and <b>hWindow</b> handles must refer to two different primary allocations of the same size, the device in the <b>hDevice</b> member must own the video present source that is identified by the <b>VidPnSourceId</b> member, and the <b>SrcRectValid</b> bit-field flag must be set in the <b>Flags</b> member. </p>
</dd>

### -field <b>Color</b>

<dd>
<p>[in] The ARGB 32-bit (see the <a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a> enumeration) color-fill or color-key value . A value for color fill is set when the <b>ColorFill</b> bit-field flag is set in the <b>Flags</b> member. A value for color key is set when either the <b>SrcColorKey</b> or <b>DstColorKey</b> bit-field flag is set in the <b>Flags</b> member. Note that only one of the <b>ColorFill</b>, <b>SrcColorKey</b>, and <b>DstColorKey</b> bit-field flags is set at any time. </p>
<p>If the primary format is palettized RGB, <b>Color</b> contains the palette index rather than the D3DDDIFMT_A8R8G8B8 value from D3DDDIFORMAT. </p>
</dd>

### -field <b>DstRect</b>

<dd>
<p>[in] The optional destination <a href="display.rect">RECT</a> for the bitblt. The destination RECT is used only if the <b>DstRectValid</b> bit-field flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>SrcRect</b>

<dd>
<p>[in] The optional source RECT for the bitblt. The source RECT is used only if the <b>SrcRectValid</b> bit-field flag is set in the <b>Flags</b> member. </p>
</dd>

### -field <b>SubRectCnt</b>

<dd>
<p>[in] The number of subrectangular regions that <b>pSrcSubRects</b> points to that are specified when presenting.</p>
</dd>

### -field <b>pSrcSubRects</b>

<dd>
<p>[in] A pointer to an array of subrectangular regions (RECTs) that are specified when presenting.</p>
</dd>

### -field <b>PresentCount</b>

<dd>
<p>[in] The number of present operations that can be queued for the device that is specified by <b>hDevice</b>.</p>
</dd>

### -field <b>FlipInterval</b>

<dd>
<p>[in] A <a href="..\d3dukmdt\ne-d3dukmdt-d3dddi-flipinterval-type.md">D3DDDI_FLIPINTERVAL_TYPE</a>-typed value that indicates the flip interval (that is, if the flip occurs after zero, one, two, three, or four vertical syncs). </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-presentflags.md">D3DKMT_PRESENTFLAGS</a> structure that identifies, in bit-field flags, how to display. Note that the <b>ColorFill</b>, <b>SrcColorKey</b>, and <b>DstColorKey</b> bit-field flags are mutually exclusive.</p>
</dd>

### -field <b>BroadcastContextCount</b>

<dd>
<p>[in] The number of additional contexts in the array that <b>BroadcastContext</b> specifies.</p>
</dd>

### -field <b>BroadcastContext</b>

<dd>
<p>[in] An array of D3DKMT_HANDLE data types that represent kernel-mode handles to the additional contexts to broadcast the current present operation to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of contexts that the OpenGL ICD can broadcast the current present operation to.</p>
<p>Broadcasting is supported only for flip operations. To broadcast a flip operation, the display miniport driver must support memory mapped I/O (MMIO)-based flips. To indicate support of MMIO flips, the display miniport driver sets the <b>FlipOnVSyncMmIo</b> bit-field flag in the <b>FlipCaps</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a> structure when its <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function is called.</p>
<p>The original context that the <b>hContext</b> member specifies and that the OpenGL ICD presents to is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the OpenGL ICD sends the present operation to the owning context (<b>hContext</b>) and broadcasts to that one additional context. </p>
</dd>

### -field <b>PresentLimitSemaphore</b>

<dd>
<p>[in] The handle to the present-limit semaphore.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>PresentHistoryToken</b>

<dd>
<p>[in] A <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-presenthistorytoken.md">D3DKMT_PRESENTHISTORYTOKEN</a> structure that identifies the type of present operation.</p>
<p>Supported starting with Windows 7.</p>
</dd>

### -field <b>pPresentRegions</b>

<dd>
<p>A pointer to a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-present-rgns.md">D3DKMT_PRESENT_RGNS</a> structure that identifies dirty and move regions.</p>
<p>Supported starting with Windows 8.</p>
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
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dukmdt\ne-d3dukmdt--d3dddiformat.md">D3DDDIFORMAT</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-present-rgns.md">D3DKMT_PRESENT_RGNS</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-presentflags.md">D3DKMT_PRESENTFLAGS</a>
</dt>
<dt>
<a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-presenthistorytoken.md">D3DKMT_PRESENTHISTORYTOKEN</a>
</dt>
<dt>
<a href="..\d3dkmthk\nf-d3dkmthk-d3dkmtpresent.md">D3DKMTPresent</a>
</dt>
<dt>
<a href="display.rect">RECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_PRESENT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
