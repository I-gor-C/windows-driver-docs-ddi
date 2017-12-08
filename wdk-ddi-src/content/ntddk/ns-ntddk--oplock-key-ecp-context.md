---
UID: NS.ntddk._OPLOCK_KEY_ECP_CONTEXT
title: OPLOCK_KEY_ECP_CONTEXT
author: windows-driver-content
description: The OPLOCK_KEY_ECP_CONTEXT structure is used to attach an oplock key to a file.
old-location: ifsk\oplock_key_ecp_context.htm
old-project: ifsk
ms.assetid: 029dd105-162a-4674-a3d5-b54a91fa4be2
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: OPLOCK_KEY_ECP_CONTEXT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddk.h
req.include-header: Ntifs.h, Ntddk.h
req.target-type: Windows
req.target-min-winverclnt: This structure is available starting with Windows 7.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OPLOCK_KEY_ECP_CONTEXT
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# OPLOCK_KEY_ECP_CONTEXT structure



## -description
<p>The OPLOCK_KEY_ECP_CONTEXT structure is used to attach an oplock key to a file. </p>


## -syntax

````
typedef struct _OPLOCK_KEY_ECP_CONTEXT {
  GUID  OplockKey;
  ULONG Reserved;
} OPLOCK_KEY_ECP_CONTEXT, *POPLOCK_KEY_ECP_CONTEXT;
````


## -struct-fields
<dl>

### -field OplockKey

<dd>
<p>A GUID for the oplock key. This GUID is shared among different handles and identifies them as belonging to the same client cache. When two handles share the same oplock key, a request performed on one handle will not break an outstanding oplock on the other handle. </p>
</dd>

### -field Reserved

<dd>
<p>Reserved. Must be set to zero. </p>
</dd>
</dl>

## -remarks
<p>For information about how to use ECPs to associate extra information with a file when the file is created, see <a href="ifsk.using_extra_create_parameters_with_an_irp_mj_create_operation">Using Extra Create Parameters with an IRP_MJ_CREATE Operation</a>. </p>

<p>The OPLOCK_KEY_ECP_CONTEXT structure is read-only. You should use it to retrieve information about the oplock key ECP only. For more information about this issue, see <a href="ifsk.system_defined_ecps">System-Defined ECPs</a>.</p>

<p>The oplock key enables an application to open multiple handles to the same stream without breaking the application's own oplock. The oplock break only occurs after the application receives a sharing violation (STATUS_SHARING_VIOLATION). </p>

<p>Oplocks are granted on stream handles when a stream is opened. Such a stream handle can be associated with an oplock key. A caller can explicitly provide the oplock key to the <a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a> routine to create the stream handle. If the caller does not explicitly specify an oplock key when the caller creates the handle, the operating system treats the handle as having a unique oplock key associated with the handle, so that the handle's key differs from any other key on any other handle. If a file operation is received on a handle other than the one on which the oplock was granted, and the oplock key that is associated with the oplock's handle differs from the key that is associated with the operation's handle, and that operation is incompatible with the currently granted oplock, then that oplock is broken. The oplock breaks even if it is the same process or thread performing the incompatible operation. For example, if a process opens a stream for which an exclusive oplock is granted and the same process then opens the same stream again, by using a different (or no) oplock key, the exclusive oplock is broken immediately.</p>

<p>Oplock keys are associated with handles when the handles are created. You can associate a handle with an oplock key even if no oplocks are granted.</p>

<p>For more information about oplocks and oplock keys, see <a href="https://msdn.microsoft.com/e9a45ae0-0ec8-4d6c-8486-ae88bdaa1f8c">Oplock Semantics Overview</a>. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>This structure is available starting with Windows 7. </p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h or Ntddk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20OPLOCK_KEY_ECP_CONTEXT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
