---
UID: NS.ntddk._WHEA_ERROR_RECORD_HEADER_VALIDBITS
title: WHEA_ERROR_RECORD_HEADER_VALIDBITS
author: windows-driver-content
description: The WHEA_ERROR_RECORD_HEADER_VALIDBITS union describes which members of a WHEA_ERROR_RECORD_HEADER structure contain valid data.
old-location: whea\whea_error_record_header_validbits.htm
ms.assetid: b16dd19f-1a67-4066-9dae-b36ff6f44d43
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: whea
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WHEA_ERROR_RECORD_HEADER_VALIDBITS
req.alt-loc: ntddk.h
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
ms.keywords: WHEA_ERROR_RECORD_HEADER_VALIDBITS, WHEA_ERROR_RECORD_HEADER_VALIDBITS, *PWHEA_ERROR_RECORD_HEADER_VALIDBITS
req.iface: 
---

# WHEA_ERROR_RECORD_HEADER_VALIDBITS structure



## -description
<p>The WHEA_ERROR_RECORD_HEADER_VALIDBITS union describes which members of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a> structure contain valid data.</p>


## -syntax

````
typedef union _WHEA_ERROR_RECORD_HEADER_VALIDBITS {
  struct {
    ULONG PlatformId  :1;
    ULONG Timestamp  :1;
    ULONG PartitionId  :1;
    ULONG Reserved  :29;
  };
  ULONG  AsULONG;
} WHEA_ERROR_RECORD_HEADER_VALIDBITS, *PWHEA_ERROR_RECORD_HEADER_VALIDBITS;
````


## -struct-fields
<dl>

### -field <b>PlatformId</b>

<dd>
<p>A single bit that indicates that the <b>PlatformId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>

### -field <b>Timestamp</b>

<dd>
<p>A single bit that indicates that the <b>Timestamp</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>

### -field <b>PartitionId</b>

<dd>
<p>A single bit that indicates that the <b>PartitionId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for system use.</p>
</dd>

### -field <b>AsULONG</b>

<dd>
<p>A ULONG representation of the contents of the WHEA_ERROR_RECORD_HEADER_VALIDBITS union.</p>
</dd>
</dl>

## -remarks
<p>A WHEA_ERROR_RECORD_HEADER_VALIDBITS union is contained within the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a> structure.</p><p class="note">If you build your <a href="https://msdn.microsoft.com/fb559ac3-1f8d-48b7-8ebe-018623ab8d09">Windows hardware error architecture (WHEA) user-mode application</a> or <a href="https://msdn.microsoft.com/473d9206-9db2-4bc7-bc76-6be2fb77b20b">platform-specific hardware error driver (PSHED) plug-in</a> with the header files from the Windows Server 2008 version of the WDK or Windows SDK, you will have trouble only if your application or PSHED plug-in accesses the <b>Timestamp</b> and <b>PlatformId</b> members directly when it processes the contents of a WHEA_ERROR_RECORD_HEADER structure. When you test these bits in the <b>AsULONG </b>member through the bitfield constants that are described in the following list, you will always produce the correct results.</p><p class="note">This problem has been fixed in the Windows 7 version of the WDK and SDK.</p>

<p>The following bitfield constants can be used to test the bits in the <b>AsULONG </b>member:</p>

<p></p><dl>
<dt><a id="WHEA_ERROR_RECORD_VALID_PLATFORMID"></a><a id="whea_error_record_valid_platformid"></a>WHEA_ERROR_RECORD_VALID_PLATFORMID</dt>
<dd>
<p>If this bit is set, it indicates that the <b>PlatformId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>
<dt><a id="WHEA_ERROR_RECORD_VALID_TIMESTAMP"></a><a id="whea_error_record_valid_timestamp"></a>WHEA_ERROR_RECORD_VALID_TIMESTAMP</dt>
<dd>
<p>If this bit is set, it indicates that the <b>Timestamp</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>
<dt><a id="WHEA_ERROR_RECORD_VALID_PARTITIONID"></a><a id="whea_error_record_valid_partitionid"></a>WHEA_ERROR_RECORD_VALID_PARTITIONID</dt>
<dd>
<p>If this bit is set, it indicates that the <b>PartitionId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>
</dd>
</dl><p>If this bit is set, it indicates that the <b>PlatformId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>

<p>If this bit is set, it indicates that the <b>Timestamp</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>

<p>If this bit is set, it indicates that the <b>PartitionId</b> member of the WHEA_ERROR_RECORD_HEADER structure contains valid data.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2008, Windows Vista SP1, and later versions of Windows.
</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h (include Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560487">WHEA_ERROR_RECORD_HEADER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [whea\whea]:%20WHEA_ERROR_RECORD_HEADER_VALIDBITS union%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
