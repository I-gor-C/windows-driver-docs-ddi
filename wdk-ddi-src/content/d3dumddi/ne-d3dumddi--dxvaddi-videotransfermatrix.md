---
UID: NE.d3dumddi._DXVADDI_VIDEOTRANSFERMATRIX
title: DXVADDI_VIDEOTRANSFERMATRIX
author: windows-driver-content
description: The DXVADDI_VIDEOTRANSFERMATRIX enumeration type contains values that identify the conversion matrix from Y'Cb'Cr' to (studio) R'G'B'.
old-location: display\dxvaddi_videotransfermatrix.htm
old-project: display
ms.assetid: ef1f3c9b-70e5-48bd-b9f4-60ec661dc880
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVADDI_VIDEOTRANSFERMATRIX
req.alt-loc: d3dumddi.h
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

# DXVADDI_VIDEOTRANSFERMATRIX enumeration



## -description
<p>The DXVADDI_VIDEOTRANSFERMATRIX enumeration type contains values that identify the conversion matrix from Y'Cb'Cr' to (studio) R'G'B'.</p>


## -syntax

````
typedef enum _DXVADDI_VIDEOTRANSFERMATRIX { 
  DXVADDI_VideoTransferMatrixMask        = 0x07,
  DXVADDI_VideoTransferMatrix_Unknown    = 0,
  DXVADDI_VideoTransferMatrix_BT709      = 1,
  DXVADDI_VideoTransferMatrix_BT601      = 2,
  DXVADDI_VideoTransferMatrix_SMPTE240M  = 3
} DXVADDI_VIDEOTRANSFERMATRIX;
````


## -enum-fields
<dl>

### -field <a id="DXVADDI_VideoTransferMatrixMask"></a><a id="dxvaddi_videotransfermatrixmask"></a><a id="DXVADDI_VIDEOTRANSFERMATRIXMASK"></a><b>DXVADDI_VideoTransferMatrixMask</b>

<dd>
<p>Specifies the video transfer matrix mask. The first 3 (0x07) bits of a DWORD can be used to specify video transfer matrix.</p>
</dd>

### -field <a id="DXVADDI_VideoTransferMatrix_Unknown"></a><a id="dxvaddi_videotransfermatrix_unknown"></a><a id="DXVADDI_VIDEOTRANSFERMATRIX_UNKNOWN"></a><b>DXVADDI_VideoTransferMatrix_Unknown</b>

<dd>
<p>Specifies that the video transfer matrix is not specified. The default value is BT601 for standard definition (SD) video and BT709 for high definition (HD) video.</p>
</dd>

### -field <a id="DXVADDI_VideoTransferMatrix_BT709"></a><a id="dxvaddi_videotransfermatrix_bt709"></a><a id="DXVADDI_VIDEOTRANSFERMATRIX_BT709"></a><b>DXVADDI_VideoTransferMatrix_BT709</b>

<dd>
<p>Specifies the BT709 transfer matrix.</p>
</dd>

### -field <a id="DXVADDI_VideoTransferMatrix_BT601"></a><a id="dxvaddi_videotransfermatrix_bt601"></a><a id="DXVADDI_VIDEOTRANSFERMATRIX_BT601"></a><b>DXVADDI_VideoTransferMatrix_BT601</b>

<dd>
<p>Specifies the BT601 transfer matrix.</p>
</dd>

### -field <a id="DXVADDI_VideoTransferMatrix_SMPTE240M"></a><a id="dxvaddi_videotransfermatrix_smpte240m"></a><a id="DXVADDI_VIDEOTRANSFERMATRIX_SMPTE240M"></a><b>DXVADDI_VideoTransferMatrix_SMPTE240M</b>

<dd>
<p>Specifies a HD video standard that is rarely used in Japan.</p>
</dd>
</dl>

## -remarks
<p>One of the values of DXVADDI_VIDEOTRANSFERMATRIX can be specified in the <b>VideoTransferMatrix</b> member of the <a href="..\d3dumddi\ns-d3dumddi--dxvaddi-extendedformat.md">DXVADDI_EXTENDEDFORMAT</a> structure.</p>

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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\ns-d3dumddi--dxvaddi-extendedformat.md">DXVADDI_EXTENDEDFORMAT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXVADDI_VIDEOTRANSFERMATRIX enumeration%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
