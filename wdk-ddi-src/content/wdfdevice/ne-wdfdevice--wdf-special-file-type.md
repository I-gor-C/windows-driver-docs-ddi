---
UID: NE.wdfdevice._WDF_SPECIAL_FILE_TYPE
title: WDF_SPECIAL_FILE_TYPE
author: windows-driver-content
description: The WDF_SPECIAL_FILE_TYPE enumeration identifies special file types that a device can support.
old-location: wdf\wdf_special_file_type.htm
old-project: wdf
ms.assetid: 3879570f-e083-4eaf-aa5b-9b78d8f826c1
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_REL_TIMEOUT_IN_US
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_SPECIAL_FILE_TYPE
req.alt-loc: wdfdevice.h
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
req.product: Windows 10 or later.
---

# WDF_SPECIAL_FILE_TYPE enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_SPECIAL_FILE_TYPE</b> enumeration identifies special file types that a device can support.</p>


## -syntax

````
typedef enum _WDF_SPECIAL_FILE_TYPE { 
  WdfSpecialFileUndefined    = 0,
  WdfSpecialFilePaging       = 1,
  WdfSpecialFileHibernation  = 2,
  WdfSpecialFileDump         = 3,
  WdfSpecialFileBoot         = 4,
  WdfSpecialFileMax          = 5
} WDF_SPECIAL_FILE_TYPE, *PWDF_SPECIAL_FILE_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WdfSpecialFileUndefined"></a><a id="wdfspecialfileundefined"></a><a id="WDFSPECIALFILEUNDEFINED"></a><b>WdfSpecialFileUndefined</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WdfSpecialFilePaging"></a><a id="wdfspecialfilepaging"></a><a id="WDFSPECIALFILEPAGING"></a><b>WdfSpecialFilePaging</b>

<dd>
<p>The device supports paging files.</p>
</dd>

### -field <a id="WdfSpecialFileHibernation"></a><a id="wdfspecialfilehibernation"></a><a id="WDFSPECIALFILEHIBERNATION"></a><b>WdfSpecialFileHibernation</b>

<dd>
<p>The device supports hibernation files.</p>
</dd>

### -field <a id="WdfSpecialFileDump"></a><a id="wdfspecialfiledump"></a><a id="WDFSPECIALFILEDUMP"></a><b>WdfSpecialFileDump</b>

<dd>
<p>The device supports dump files.</p>
</dd>

### -field <a id="WdfSpecialFileBoot"></a><a id="wdfspecialfileboot"></a><a id="WDFSPECIALFILEBOOT"></a><b>WdfSpecialFileBoot</b>

<dd>
<p>The device supports boot files. This constant is available in version 1.11 and later versions of KMDF.</p>
</dd>

### -field <a id="WdfSpecialFileMax"></a><a id="wdfspecialfilemax"></a><a id="WDFSPECIALFILEMAX"></a><b>WdfSpecialFileMax</b>

<dd>
<p>For internal use only.</p>
</dd>
</dl>

## -remarks
<p>For more information, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>

<p>For more information, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>

<p>For more information, see <a href="wdf.supporting_special_files">Supporting Special Files</a>.</p>

## -requirements
<table>
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
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546903">WdfDeviceSetSpecialFileSupport</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_SPECIAL_FILE_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
