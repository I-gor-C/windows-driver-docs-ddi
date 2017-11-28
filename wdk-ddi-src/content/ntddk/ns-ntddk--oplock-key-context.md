---
UID: NS.ntddk._OPLOCK_KEY_CONTEXT
title: OPLOCK_KEY_CONTEXT
author: windows-driver-content
description: The OPLOCK_KEY_CONTEXT structure is returned from IoGetOplockKeyContextEx. This structure contains oplock keys for a specific file object.
old-location: ifsk\oplock_key_context.htm
old-project: ifsk
ms.assetid: E6A61B8F-CB43-4858-B5CF-32DD022A569E
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: OPLOCK_KEY_CONTEXT, OPLOCK_KEY_CONTEXT, *POPLOCK_KEY_CONTEXT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPLOCK_KEY_CONTEXT
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
req.iface: 
---

# OPLOCK_KEY_CONTEXT structure



## -description
<p>The <b>OPLOCK_KEY_CONTEXT</b> structure is returned from <a href="https://msdn.microsoft.com/library/windows/hardware/hh439325">IoGetOplockKeyContextEx</a>. This structure contains oplock keys for a specific file object.</p>


## -syntax

````
typedef struct _OPLOCK_KEY_CONTEXT {
  ULONG Version  :8;
  ULONG Flags  :8;
  GUID  ParentOplockKey;
  GUID  TargetOplockKey;
} OPLOCK_KEY_CONTEXT, *POPLOCK_KEY_CONTEXT;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The oplock key version. The version is set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="OPLOCK_KEY_VERSION_WIN7"></a><a id="oplock_key_version_win7"></a><dl>

### -field <b>OPLOCK_KEY_VERSION_WIN7</b>

</dl>
</td>
<td width="60%">
<p>This is a Windows 7 oplock key.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="OPLOCK_KEY_VERSION_WIN8"></a><a id="oplock_key_version_win8"></a><dl>

### -field <b>OPLOCK_KEY_VERSION_WIN8</b>

</dl>
</td>
<td width="60%">
<p>This is a Windows 8 oplock key.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A set of flags that indicate the oplock key type. <b>Flags</b> is set to one or both of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="OPLOCK_KEY_FLAG_PARENT_KEY"></a><a id="oplock_key_flag_parent_key"></a><dl>

### -field <b>OPLOCK_KEY_FLAG_PARENT_KEY</b>

</dl>
</td>
<td width="60%">
<p>A valid oplock key is present in <b>ParentOplockKey.</b></p>
</td>
</tr>
<tr>
<td width="40%"><a id="OPLOCK_KEY_FLAG_TARGET_KEY"></a><a id="oplock_key_flag_target_key"></a><dl>

### -field <b>OPLOCK_KEY_FLAG_TARGET_KEY</b>

</dl>
</td>
<td width="60%">
<p>A valid oplock key is present in <b>TargetOplockKey.</b></p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ParentOplockKey</b>

<dd>
<p>A <b>GUID</b>  that represents the parent oplock  key value.</p>
</dd>

### -field <b>TargetOplockKey</b>

<dd>
<p>A <b>GUID</b>  that represents the target oplock  key value.</p>
</dd>
</dl>

## -remarks
<p>If an oplock is requested for a file during an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548630">IRP_MJ_CREATE</a> request, a file system that supports oplocks   will attach an oplock key context to the file object created. The oplock key  context is later available through a pointer to an <b>OPLOCK_KEY_CONTEXT</b> structure.  The <b>OPLOCK_KEY_CONTEXT</b> structure is returned from a call to <a href="https://msdn.microsoft.com/library/windows/hardware/hh439325">IoGetOplockKeyContextEx</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting in Windows 8.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406392">DUAL_OPLOCK_KEY_ECP_CONTEXT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439325">IoGetOplockKeyContextEx</a>
</dt>
<dt>
<a href="ifsk.oplock_semantics">Oplock Semantics</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20OPLOCK_KEY_CONTEXT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
