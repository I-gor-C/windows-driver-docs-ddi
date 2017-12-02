---
UID: NE.fltuserstructures._FLT_FILESYSTEM_TYPE
title: FLT_FILESYSTEM_TYPE
author: windows-driver-content
description: The FLT_FILESYSTEM_TYPE enumeration identifies the type of file system being used on a volume.
old-location: ifsk\flt_filesystem_type.htm
old-project: ifsk
ms.assetid: b4bdfa93-3db5-4dfa-b539-112927cbedb0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FLT_VOLUME_PROPERTIES, FLT_VOLUME_PROPERTIES, *PFLT_VOLUME_PROPERTIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: fltuserstructures.h
req.include-header: FltUser.h, FltKernel.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FLT_FILESYSTEM_TYPE
req.alt-loc: fltUserStructures.h
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

# FLT_FILESYSTEM_TYPE enumeration



## -description
<p>The <b>FLT_FILESYSTEM_TYPE</b> enumeration identifies the type of file system being used on a volume. </p>


## -syntax

````
typedef enum _FLT_FILESYSTEM_TYPE { 
  FLT_FSTYPE_UNKNOWN,
  FLT_FSTYPE_RAW,
  FLT_FSTYPE_NTFS,
  FLT_FSTYPE_FAT,
  FLT_FSTYPE_CDFS,
  FLT_FSTYPE_UDFS,
  FLT_FSTYPE_LANMAN,
  FLT_FSTYPE_WEBDAV,
  FLT_FSTYPE_RDPDR,
  FLT_FSTYPE_NFS,
  FLT_FSTYPE_MS_NETWARE,
  FLT_FSTYPE_NETWARE,
  FLT_FSTYPE_BSUDF,
  FLT_FSTYPE_MUP,
  FLT_FSTYPE_RSFX,
  FLT_FSTYPE_ROXIO_UDF1,
  FLT_FSTYPE_ROXIO_UDF2,
  FLT_FSTYPE_ROXIO_UDF3,
  FLT_FSTYPE_TACIT,
  FLT_FSTYPE_FS_REC,
  FLT_FSTYPE_INCD,
  FLT_FSTYPE_INCD_FAT,
  FLT_FSTYPE_EXFAT,
  FLT_FSTYPE_PSFS,
  FLT_FSTYPE_GPFS,
  FLT_FSTYPE_NPFS,
  FLT_FSTYPE_MSFS,
  FLT_FSTYPE_CSVFS,
  FLT_FSTYPE_REFS,
  FLT_FSTYPE_OPENAFS
} FLT_FILESYSTEM_TYPE, *PFLT_FILESYSTEM_TYPE;
````


## -enum-fields
<dl>

### -field FLT_FSTYPE_UNKNOWN

<dd>
<p>Unknown file system type.</p>
</dd>

### -field FLT_FSTYPE_RAW

<dd>
<p>Microsoft RAW file system. File system namespace: \FileSystem\RAW. </p>
</dd>

### -field FLT_FSTYPE_NTFS

<dd>
<p>Microsoft NTFS file system. File system namespace:  \FileSystem\Ntfs.</p>
</dd>

### -field FLT_FSTYPE_FAT

<dd>
<p>Microsoft FAT file system. File system namespace: \FileSystem\Fastfat. </p>
</dd>

### -field FLT_FSTYPE_CDFS

<dd>
<p>Microsoft CDFS file system. File system namespace: \FileSystem\Cdfs.</p>
</dd>

### -field FLT_FSTYPE_UDFS

<dd>
<p>Microsoft UDFS file system. File system namespace: \FileSystem\Udfs.</p>
</dd>

### -field FLT_FSTYPE_LANMAN

<dd>
<p>Microsoft LanMan Redirector. File system namespace: \FileSystem\MRxSmb.</p>
</dd>

### -field FLT_FSTYPE_WEBDAV

<dd>
<p>Microsoft WebDav redirector. File system namespace: \FileSystem\MRxDav.</p>
</dd>

### -field FLT_FSTYPE_RDPDR

<dd>
<p>Microsoft Terminal Server redirector. File system namespace: \Driver\rdpdr.</p>
</dd>

### -field FLT_FSTYPE_NFS

<dd>
<p>Microsoft NFS file system. File system namespace: \FileSystem\NfsRdr.</p>
</dd>

### -field FLT_FSTYPE_MS_NETWARE

<dd>
<p>Microsoft NetWare redirector. File system namespace: \FileSystem\nwrdr.</p>
</dd>

### -field FLT_FSTYPE_NETWARE

<dd>
<p>Novell NetWare redirector.</p>
</dd>

### -field FLT_FSTYPE_BSUDF

<dd>
<p>The BsUDF CD-ROM driver. File system namespace: \FileSystem\BsUDF.</p>
</dd>

### -field FLT_FSTYPE_MUP

<dd>
<p>Microsoft MUP redirector. File system namespace: \FileSystem\Mup.</p>
</dd>

### -field FLT_FSTYPE_RSFX

<dd>
<p>Microsoft WinFS redirector. File system namespace: \FileSystem\RsFxDrv.</p>
</dd>

### -field FLT_FSTYPE_ROXIO_UDF1

<dd>
<p>Roxio UDF writeable file system. File system namespace: \FileSystem\cdudf_xp.</p>
</dd>

### -field FLT_FSTYPE_ROXIO_UDF2

<dd>
<p>Roxio UDF readable file system. File system namespace: \FileSystem\UdfReadr_xp.</p>
</dd>

### -field FLT_FSTYPE_ROXIO_UDF3

<dd>
<p>Roxio DVD file system. File system namespace: \FileSystem\DVDVRRdr_xp.</p>
</dd>

### -field FLT_FSTYPE_TACIT

<dd>
<p>Tacit file system. Namespace: \Device\TCFSPSE.</p>
</dd>

### -field FLT_FSTYPE_FS_REC

<dd>
<p>Microsoft file system recognizer. File system namespace: \FileSystem\Fs_rec.</p>
</dd>

### -field FLT_FSTYPE_INCD

<dd>
<p>Nero InCD file system. File system namespace: \FileSystem\InCDfs.</p>
</dd>

### -field FLT_FSTYPE_INCD_FAT

<dd>
<p>Nero InCD FAT file system. File system namespace: \FileSystem\InCDFat.</p>
</dd>

### -field FLT_FSTYPE_EXFAT

<dd>
<p>Microsoft EXFat file system. File system namespace: \FileSystem\exfat.</p>
</dd>

### -field FLT_FSTYPE_PSFS

<dd>
<p>PolyServ file system. File system namespace: \FileSystem\psfs.</p>
</dd>

### -field FLT_FSTYPE_GPFS

<dd>
<p>IBM General Parallel File System. File system namespace: \FileSystem\gpfs.</p>
</dd>

### -field FLT_FSTYPE_NPFS

<dd>
<p>Microsoft named pipe file system. File system namespace: \FileSystem\npfs.</p>
</dd>

### -field FLT_FSTYPE_MSFS

<dd>
<p>Microsoft mailslot file system. File system namespace: \FileSystem\msfs.</p>
</dd>

### -field FLT_FSTYPE_CSVFS

<dd>
<p>Microsoft cluster shared volume file system. File system namespace: \FileSystem\csvfs.</p>
</dd>

### -field FLT_FSTYPE_REFS

<dd>
<p>Microsoft ReFS file system. File system namespace: \FileSystem\refs.</p>
</dd>

### -field FLT_FSTYPE_OPENAFS

<dd>
<p> OpenAFS file system. File system namespace: \FileSystem\AFSRedirector.</p>
</dd>
</dl>

## -remarks
<p>New file systems that are not part of the <b>FLT_FILESYSTEM_TYPE</b> enumeration are treated as <b>FLT_FSTYPE_UNKNOWN</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>FltUserStructures.h (include FltUser.h or FltKernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--filter-volume-standard-information.md">FILTER_VOLUME_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetfilesystemtype.md">FltGetFileSystemType</a>
</dt>
<dt>
<a href="..\fltuserstructures\ns-fltuserstructures--instance-aggregate-standard-information.md">INSTANCE_AGGREGATE_STANDARD_INFORMATION</a>
</dt>
<dt>
<a href="..\fltkernel\nc-fltkernel-pflt-instance-setup-callback.md">PFLT_INSTANCE_SETUP_CALLBACK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FLT_FILESYSTEM_TYPE enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
