---
UID: NF.storport.StorPortGetPfns
title: StorPortGetPfns
author: windows-driver-content
description: The StorPortGetPfns routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB.
old-location: storage\storportgetpfns.htm
old-project: storage
ms.assetid: F9E69501-4889-4A1B-8942-C6D4406474DE
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: StorPortGetPfns
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: storport.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: StorPortGetPfns
req.alt-loc: Storport.h
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
req.product: Windows 10 or later.
---

# StorPortGetPfns function



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>The <b>StorPortGetPfns</b> routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB
</p>


## -syntax

````
ULONG StorPortGetPfns(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _In_  PVOID               Mdl,
  _Out_ PVOID*              Pfns,
  _Out_ ULONG*              PfnCount,
  _Out_ ULONG*              StartingOffset
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver.</p>
</dd>

### -param <i>Srb</i> [in]

<dd>
<p>A pointer to the source SCSI request block (SRB). </p>
</dd>

### -param <i>Mdl</i> [in]

<dd>
<p>A pointer to the MDL for which Pfns are requested. Only MDLs obtained 
            using <b>StorPortGetOriginalMdl</b> or <b>StorPortGetDataInBufferMdl</b> are supported.</p>
</dd>

### -param <i>Pfns</i> [out]

<dd>
<p> A pointer to the beginning of the array of physical page numbers that are associated with the MDL.
              Callers must NOT modify or update or free the list.</p>
</dd>

### -param <i>PfnCount</i> [out]

<dd>
<p>Specifies the number of PFNs in the array.</p>
</dd>

### -param <i>StartingOffset</i> [out]

<dd>
<p>Specifies the byte offset within the initial page of the buffer described by the given MDL.</p>
</dd>
</dl>

## -returns
<p><b>StorPortGetPfns</b> returns one of the following status codes:</p><dl>
<dt><b>STOR_STATUS_NOT_IMPLEMENTED</b></dt>
</dl><p>This function is not implemented on the active operating system.</p><dl>
<dt><b>STOR_STATUS_SUCCESS</b></dt>
</dl><p>The list items were removed successfully or the list is already empty.</p><dl>
<dt><b>STOR_STATUS_INVALID_PARAMETER</b></dt>
</dl><p>A pointer to one of the parameters  is <b>NULL</b>.</p>

<p> </p>

## -remarks
<p> Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver in the <b>DeviceExtension-&gt;HwDeviceExtension</b> member of the device object for the HBA immediately after the miniport driver calls <a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>. The port driver frees this memory when it removes the device. </p>

<p>Starting in Windows 8, the <i>Srb</i> parameter may point to either <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> or <a href="..\srb\ns-srb--storage-request-block.md">STORAGE_REQUEST_BLOCK</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Storport.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/jj553718">StorPortGetDataInBufferMdl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567093">StorPortGetOriginalMdl</a>
</dt>
<dt>
<a href="..\storport\nf-storport-storportinitialize.md">StorPortInitialize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20StorPortGetPfns routine%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
