---
UID: NS.ntifs._WIM_PROVIDER_EXTERNAL_INFO
title: WIM_PROVIDER_EXTERNAL_INFO
author: windows-driver-content
description: The WIM_PROVIDER_EXTERNAL_INFO structure holds the identifier and status information for the Windows Image File (WIM) external backing provider.
old-location: ifsk\wim_provider_external_info.htm
ms.assetid: CD51FBD6-A589-4135-8BF0-8F0075654A05
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: ifsk
req.header: ntifs.h
req.include-header: Ntifs.h, Fltkernel.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 8.1 Update.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WIM_PROVIDER_EXTERNAL_INFO
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
ms.keywords: WIM_PROVIDER_EXTERNAL_INFO, WIM_PROVIDER_EXTERNAL_INFO, *PWIM_PROVIDER_EXTERNAL_INFO
req.iface: 
---

# WIM_PROVIDER_EXTERNAL_INFO structure



## -description
<p>The <b>WIM_PROVIDER_EXTERNAL_INFO</b> structure holds the identifier and status information for the Windows Image File (WIM) external backing provider. </p>


## -syntax

````
typedef struct _WIM_PROVIDER_EXTERNAL_INFO {
  ULONG         Version;
  ULONG         Flags;
  LARGE_INTEGER DataSourceId;
  UCHAR         ResourceHash[WIM_PROVIDER_HASH_SIZE];
} WIM_PROVIDER_EXTERNAL_INFO, *PWIM_PROVIDER_EXTERNAL_INFO;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The WIM provider version. Set to WIM_PROVIDER_CURRENT_VERSION.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The status flags for the WIM provider. Set to 0 when active. Otherwise <b>Flags</b> is set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="WIM_PROVIDER_EXTERNAL_FLAG_NOT_ACTIVE"></a><a id="wim_provider_external_flag_not_active"></a><dl>

### -field <b>WIM_PROVIDER_EXTERNAL_FLAG_NOT_ACTIVE</b>

</dl>
</td>
<td width="60%">
<p>The WIM provider is not active. This can occur when the WIM file is  not found. In this case the WIM file will not be recovered.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="WIM_PROVIDER_EXTERNAL_FLAG_SUSPENDED"></a><a id="wim_provider_external_flag_suspended"></a><dl>

### -field <b>WIM_PROVIDER_EXTERNAL_FLAG_SUSPENDED</b>

</dl>
</td>
<td width="60%">
<p>Indicates that the provider is dismounted. Recovery will be attempted.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>DataSourceId</b>

<dd>
<p>An identifier value for the WIM file data source.</p>
</dd>

### -field <b>ResourceHash</b>

<dd>
<p>An identifier for the object contained within the WIM.  Conventionally a hash of the contents of a file, stored within the WIM.</p>
</dd>
</dl>

## -remarks
<p>The backing source for a file is set with a <a href="https://msdn.microsoft.com/library/windows/hardware/dn632443">FSCTL_SET_EXTERNAL_BACKING</a> control code request. The WIM file backing the file specified in the request is set in the <b>DataSourceId</b> member of <b>WIM_PROVIDER_EXTERNAL_INFO</b>.</p>

<p>The <b>Flags</b> and <b>ResourceHash</b> members are valid when the provider info is returned from a <a href="https://msdn.microsoft.com/library/windows/hardware/dn632441">FSCTL_GET_EXTERNAL_BACKING</a> request.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn632441">FSCTL_GET_EXTERNAL_BACKING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn632443">FSCTL_SET_EXTERNAL_BACKING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20WIM_PROVIDER_EXTERNAL_INFO structure%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
