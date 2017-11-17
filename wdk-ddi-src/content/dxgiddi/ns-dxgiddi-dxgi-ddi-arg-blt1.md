---
UID: NS.dxgiddi.DXGI_DDI_ARG_BLT1
title: DXGI_DDI_ARG_BLT1
author: windows-driver-content
description: Describes the parameters of a bit-block transfer (bitblt) that include specifications for a source rectangle. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.
old-location: display\dxgi_ddi_arg_blt1.htm
ms.assetid: bc7c2693-6a18-4335-8921-363981a830f1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: dxgiddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8,WDDM 1.2 and later
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGI_DDI_ARG_BLT1
req.alt-loc: Dxgiddi.h
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
ms.keywords: DXGI_DDI_ARG_BLT1, DXGI_DDI_ARG_BLT1
req.iface: 
---

# DXGI_DDI_ARG_BLT1 structure



## -description
<p>Describes the parameters of a bit-block transfer (bitblt) that include specifications for a  source rectangle. Used by Windows Display Driver Model (WDDM) 1.2 and later user-mode display drivers.</p>


## -syntax

````
typedef struct DXGI_DDI_ARG_BLT1 {
  DXGI_DDI_HDEVICE       hDevice;
  DXGI_DDI_HRESOURCE     hDstResource;
  UINT                   DstSubresource;
  UINT                   DstLeft;
  UINT                   DstTop;
  UINT                   DstRight;
  UINT                   DstBottom;
  DXGI_DDI_HRESOURCE     hSrcResource;
  UINT                   SrcSubresource;
  UINT                   SrcLeft;
  UINT                   SrcTop;
  UINT                   SrcRight;
  UINT                   SrcBottom;
  DXGI_DDI_ARG_BLT_FLAGS Flags;
  DXGI_DDI_MODE_ROTATION Rotate;
} DXGI_DDI_ARG_BLT1;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] A handle to the display device (graphics context) on which the driver performs the bitblt. The Direct3D runtime passes this handle to the driver in the <b>hDrvDevice</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a> structure when the runtime calls the driver's <a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a> function to create the display device. </p>
</dd>

### -field <b>hDstResource</b>

<dd>
<p>[in] A handle to the destination resource. </p>
</dd>

### -field <b>DstSubresource</b>

<dd>
<p>[in] The index to the destination surface within the resource. </p>
</dd>

### -field <b>DstLeft</b>

<dd>
<p>[in] The <i>x</i>-coordinate of the upper-left corner of the destination rectangle. </p>
</dd>

### -field <b>DstTop</b>

<dd>
<p>[in] The <i>y</i>-coordinate of the upper-left corner of the destination rectangle. </p>
</dd>

### -field <b>DstRight</b>

<dd>
<p>[in] The <i>x</i>-coordinate of the lower-right corner of the destination rectangle. </p>
</dd>

### -field <b>DstBottom</b>

<dd>
<p>[in] The <i>y</i>-coordinate of the lower-right corner of the destination rectangle. </p>
</dd>

### -field <b>hSrcResource</b>

<dd>
<p>[in] A handle to the source resource. </p>
</dd>

### -field <b>SrcSubresource</b>

<dd>
<p>[in] The index to the source surface within the resource. </p>
</dd>

### -field <b>SrcLeft</b>

<dd>
<p>[in] The <i>x</i>-coordinate of the upper-left corner of the source rectangle.</p>
</dd>

### -field <b>SrcTop</b>

<dd>
<p>[in] The <i>y</i>-coordinate of the upper-left corner of the source rectangle. </p>
</dd>

### -field <b>SrcRight</b>

<dd>
<p>[in] The <i>x</i>-coordinate of the lower-right corner of the source rectangle.</p>
</dd>

### -field <b>SrcBottom</b>

<dd>
<p>[in] The <i>y</i>-coordinate of the lower-right corner of the destination rectangle.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] A <a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a> structure that identifies the type of bitblt to perform. </p>
</dd>

### -field <b>Rotate</b>

<dd>
<p>[in] A value of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff557502">DXGI_DDI_MODE_ROTATION</a> that identifies the orientation of the display mode.</p>
</dd>
</dl>

## -remarks
<p>The source rectangle specified by the members <b>SrcLeft</b>, <b>SrcTop</b>, <b>SrcRight</b>, and <b>SrcBottom</b> is typically a dirty subrectangle.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>WDDM 1.2 and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxgiddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/c69eedb1-c975-412c-aa9f-cf64a702f937">CreateDevice(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541664">D3D10DDIARG_CREATEDEVICE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557451">DXGI_DDI_ARG_BLT_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557502">DXGI_DDI_MODE_ROTATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGI_DDI_ARG_BLT1 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
