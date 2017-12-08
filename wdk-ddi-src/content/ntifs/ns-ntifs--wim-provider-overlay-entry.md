---
UID: NS.ntifs._WIM_PROVIDER_OVERLAY_ENTRY
title: WIM_PROVIDER_OVERLAY_ENTRY
author: windows-driver-content
description: Contains the a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume.
old-location: ifsk\wim_provider_overlay_entry.htm
old-project: ifsk
ms.assetid: 8D1C9C8B-0545-42D7-860F-E2263457E61F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WIM_PROVIDER_OVERLAY_ENTRY, WIM_PROVIDER_OVERLAY_ENTRY, *PWIM_PROVIDER_OVERLAY_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.1 Update.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIM_PROVIDER_OVERLAY_ENTRY
req.alt-loc: ntifs.h
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

# WIM_PROVIDER_OVERLAY_ENTRY structure



## -description
<p>Contains the  a Windows Image Format (WIM) file configuration information for a data source entry. It is used to identify specific WIM file names and indices that supply data to externally backed files on a volume.</p>


## -syntax

````
typedef struct _WIM_PROVIDER_OVERLAY_ENTRY {
  ULONG         NextEntryOffset;
  LARGE_INTEGER DataSourceId;
  GUID          WimGuid;
  ULONG         WimFileNameOffset;
  ULONG         WimType;
  ULONG         WimIndex;
  ULONG         Flags;
} WIM_PROVIDER_OVERLAY_ENTRY, *PWIM_PROVIDER_OVERLAY_ENTRY;
````


## -struct-fields
<dl>

### -field NextEntryOffset

<dd>
<p>The offset to the next WIM_PROVIDER_OVERLAY_ENTRY structure returned in the enumeration. Set to 0 if there are no further entries.</p>
</dd>

### -field DataSourceId

<dd>
<p>The specific identifier an overlay entry. A single WIM GUID, such as in the <b>WimGuid</b> member, may have multiple  data source identifiers.</p>
</dd>

### -field WimGuid

<dd>
<p>A unique identifier of a WIM file.</p>
</dd>

### -field WimFileNameOffset

<dd>
<p>The offset, in bytes, from the beginning of this structure of the file name for the WIM file to add as a backing source. The file name is a NULL terminated string of <b>WCHAR</b> character values.</p>
</dd>

### -field WimType

<dd>
<p>The type of WIM file set as a backing source. The WIM file type is set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="_WIM_BOOT_OS_WIM"></a><a id="_wim_boot_os_wim"></a><dl>

### -field  WIM_BOOT_OS_WIM

</dl>
</td>
<td width="60%">
<p>The WIM file contains Windows system files.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="_WIM_BOOT_NOT_OS_WIM"></a><a id="_wim_boot_not_os_wim"></a><dl>

### -field  WIM_BOOT_NOT_OS_WIM

</dl>
</td>
<td width="60%">
<p>The WIM file contains non-operating system files.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field WimIndex

<dd>
<p>The index of the image in the WIM file specified at <b>WimFileNameOffset</b>.</p>
</dd>

### -field Flags

<dd>
<p>The status flags for the WIM provider. Set to 0 when active. Otherwise <b>Flags</b> is set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WIM_PROVIDER_EXTERNAL_FLAG_NOT_ACTIVE"></a><a id="wim_provider_external_flag_not_active"></a><dl>

### -field WIM_PROVIDER_EXTERNAL_FLAG_NOT_ACTIVE

</dl>
</td>
<td width="60%">
<p>The WIM provider is not active. This can occur when the WIM file is  not found. In this case the WIM file will not be recovered.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WIM_PROVIDER_EXTERNAL_FLAG_SUSPENDED"></a><a id="wim_provider_external_flag_suspended"></a><dl>

### -field WIM_PROVIDER_EXTERNAL_FLAG_SUSPENDED

</dl>
</td>
<td width="60%">
<p>Indicates that the provider is dismounted. Recovery will be attempted.</p>
</td>
</tr>
</table>
<p> </p>
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
<p>Available starting with Windows 8.1 Update.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Fltkernel.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsctl_enum_overlay">FSCTL_ENUM_OVERLAY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20WIM_PROVIDER_OVERLAY_ENTRY structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
