---
UID: NS.ntddcdvd._DVD_COPY_PROTECT_KEY
title: DVD_COPY_PROTECT_KEY
author: windows-driver-content
description: The DVD_COPY_PROTECT_KEY structure is used in conjunction with the IOCTL_DVD_READ_KEY request to execute a report key command of the specified type.
old-location: storage\dvd_copy_protect_key.htm
ms.assetid: 79f3fdaf-e23a-40ba-a1eb-5428a63cc96a
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DVD_COPY_PROTECT_KEY
req.alt-loc: ntddcdvd.h
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
ms.keywords: DVD_COPY_PROTECT_KEY, DVD_COPY_PROTECT_KEY, *PDVD_COPY_PROTECT_KEY
req.iface: 
---

# DVD_COPY_PROTECT_KEY structure



## -description
<p>The <b>DVD_COPY_PROTECT_KEY</b> structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560425">IOCTL_DVD_READ_KEY</a> request to execute a report key command of the specified type. </p>


## -syntax

````
typedef struct _DVD_COPY_PROTECT_KEY {
  ULONG          KeyLength;
  DVD_SESSION_ID SessionId;
  DVD_KEY_TYPE   KeyType;
  ULONG          KeyFlags;
  union {
    HANDLE        FileHandle;
    LARGE_INTEGER TitleOffset;
  } Parameters;
  UCHAR          KeyData[];
} DVD_COPY_PROTECT_KEY, *PDVD_COPY_PROTECT_KEY;
````


## -struct-fields
<dl>

### -field <b>KeyLength</b>

<dd>
<p>Indicates the length of the key data to be retrieved. </p>
</dd>

### -field <b>SessionId</b>

<dd>
<p>Indicates the DVD session ID. </p>
</dd>

### -field <b>KeyType</b>

<dd>
<p>Indicates the key type. The DVD device driver uses this information to determine the key format in a report key command, as defined by the <i>SCSI Multimedia Commands - 3 (MMC-3)</i> specification. A report key command either reports key data for a specified key (challenge key, bus key, title key, RPC key, or disk key), reports the state of the authentication success flag (ASF), or invalidates an authentication grant ID (AGID). See the <i>MMC-3</i> specification for further information. </p>
</dd>

### -field <b>KeyFlags</b>

<dd>
<dl>

### -field Contains copy generation management system (CGMS) data. For devices that implement a CGMS protection scheme, the CGMS data is returned with the title key data in the <b>KeyFlags</b> member. This member can have any of the following values:


### -field 
<p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DVD_CGMS_RESERVED_MASK</p>
</td>
<td>
<p>Mask of reserved bits. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_CGMS_COPY_PROTECT_MASK</p>
</td>
<td>
<p>Copy protection bitmask. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_CGMS_COPY_PERMITTED</p>
</td>
<td>
<p>Copying is permitted, within limits of copyright restrictions. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_CGMS_COPY_ONCE</p>
</td>
<td>
<p>One generation of copies can be made.</p>
</td>
</tr>
<tr>
<td>
<p>DVD_CGMS_NO_COPY</p>
</td>
<td>
<p>No copying is allowed.</p>
</td>
</tr>
<tr>
<td>
<p>DVD_COPYRIGHT_MASK</p>
</td>
<td>
<p>Copyright bitmask. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_NOT_COPYRIGHTED</p>
</td>
<td>
<p>Copying is permitted without restriction.</p>
</td>
</tr>
<tr>
<td>
<p>DVD_COPYRIGHTED</p>
</td>
<td>
<p>Data is copyrighted. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_SECTOR_PROTECT_MASK</p>
</td>
<td>
<p>Sector protection bitmask. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_SECTOR_NOT_PROTECTED</p>
</td>
<td>
<p>Title key data is not encrypted. No decryption necessary. </p>
</td>
</tr>
<tr>
<td>
<p>DVD_SECTOR_PROTECTED</p>
</td>
<td>
<p>Title key data must be decrypted. </p>
</td>
</tr>
</table>
<p> </p>
</p>


</dl>
</dd>

### -field <b>Parameters</b>

<dd>
<dl>

### -field <b>FileHandle</b>

<dd>
<p>Pointer to the file handle for the physical device that the copy protection is being negotiated on.</p>
</dd>

### -field <b>TitleOffset</b>

<dd>
<p>Contains the logical block address on the media of the title.</p>
<p>The upper layers of the operating system use the <b>FileHandle</b> member. The file system converts the value in <b>FileHandle</b> into a logical block address and stores the result in the <b>TitleOffset</b> member. Kernel-mode drivers use the <b>TitleOffset</b> member.</p>
</dd>
</dl>
</dd>

### -field <b>KeyData</b>

<dd>
<p>Contains the key data that was returned. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553731">DVD_KEY_TYPE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560425">IOCTL_DVD_READ_KEY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20DVD_COPY_PROTECT_KEY structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
