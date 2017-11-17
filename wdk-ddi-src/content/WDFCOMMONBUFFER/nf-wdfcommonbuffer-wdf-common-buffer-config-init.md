---
UID: NF.wdfcommonbuffer.WDF_COMMON_BUFFER_CONFIG_INIT
title: WDF_COMMON_BUFFER_CONFIG_INIT
author: windows-driver-content
description: The WDF_COMMON_BUFFER_CONFIG_INIT function initializes a WDF_COMMON_BUFFER_CONFIG structure.
old-location: wdf\wdf_common_buffer_config_init.htm
ms.assetid: a678516a-159f-42bc-b135-489677452472
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfcommonbuffer.h
req.include-header: WdfCommonBuffer.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_COMMON_BUFFER_CONFIG_INIT
req.alt-loc: wdfcommonbuffer.h
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
ms.keywords: WDF_COMMON_BUFFER_CONFIG_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_COMMON_BUFFER_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_COMMON_BUFFER_CONFIG_INIT</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a> structure.</p>


## -syntax

````
VOID WDF_COMMON_BUFFER_CONFIG_INIT(
  _Out_ PWDF_COMMON_BUFFER_CONFIG Config,
  _In_  ULONG                     AlignmentRequirement
);
````


## -parameters
<dl>

### -param <i>Config</i> [out]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a> structure.</p>
</dd>

### -param <i>AlignmentRequirement</i> [in]

<dd>
<p>A value for the <b>AlignmentRequirement</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a> structure. This value specifies the alignment requirement for the common buffer that the structure describes.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_COMMON_BUFFER_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a> structure and sets the structure's <b>AlignmentRequirement</b> member to the specified value.</p>

<p>The <b>WDF_COMMON_BUFFER_CONFIG_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a> structure and sets the structure's <b>AlignmentRequirement</b> member to the specified value.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfcommonbuffer.h (include WdfCommonBuffer.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551244">WDF_COMMON_BUFFER_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_COMMON_BUFFER_CONFIG_INIT function%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
