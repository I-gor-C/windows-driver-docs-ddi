---
UID: NS.d3dkmdt._DXGKMDT_OPM_OMAC
title: DXGKMDT_OPM_OMAC
author: windows-driver-content
description: The DXGKMDT_OPM_OMAC structure contains a One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) for message authenticity.
old-location: display\dxgkmdt_opm_omac.htm
old-project: display
ms.assetid: caa64a32-3772-45b5-898a-78dc51b7f24b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGKMDT_OPM_OMAC, DXGKMDT_OPM_OMAC, *PDXGKMDT_OPM_OMAC
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGKMDT_OPM_OMAC
req.alt-loc: d3dkmdt.h
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

# DXGKMDT_OPM_OMAC structure



## -description
<p>The DXGKMDT_OPM_OMAC structure contains a One-key Cipher Block Chaining (CBC)-mode message authentication code (OMAC) for message authenticity.</p>


## -syntax

````
typedef struct _DXGKMDT_OPM_OMAC {
  BYTE abOMAC[DXGKMDT_OPM_OMAC_SIZE];
} DXGKMDT_OPM_OMAC, *PDXGKMDT_OPM_OMAC;
````


## -struct-fields
<dl>

### -field <b>abOMAC</b>

<dd>
<p>A 16-byte array that comprises the OMAC.</p>
</dd>
</dl>

## -remarks
<p>For more information about OMAC, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70417">OMAC-1 algorithm</a>. </p>

<p>The OMAC-1 parameters that OPM and COPP use are:</p>

<p><i>E</i> = AES (Advanced Encryption Standard)</p>

<p><i>t</i> = 128 bits</p>

<p><i>K</i> = The 128-bit key that the display miniport driver receives when <a href="..\dispmprt\nc-dispmprt-dxgkddi-opm-set-signing-key-and-sequence-numbers.md">DxgkDdiOPMSetSigningKeyAndSequenceNumbers</a> is called.</p>

<p><i>n</i> = 128 bits </p>

<p>For information about AES, see the <a href="http://go.microsoft.com/fwlink/p/?linkid=70411">RSA Laboratories</a> website. </p>

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
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560849">DXGKMDT_OPM_CONFIGURE_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560868">DXGKMDT_OPM_GET_INFO_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560910">DXGKMDT_OPM_REQUESTED_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKMDT_OPM_OMAC structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
