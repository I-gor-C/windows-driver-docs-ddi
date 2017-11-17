---
UID: NS.ntddchgr._CHANGER_PRODUCT_DATA
title: CHANGER_PRODUCT_DATA
author: windows-driver-content
description: The CHANGER_PRODUCT_DATA structure is used in conjunction with the IOCTL_CHANGER_GET_PRODUCT_DATA request to retrieve product data for a device.
old-location: storage\changer_product_data.htm
ms.assetid: 18e5b394-b0ea-481c-b634-83a2ebec4784
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddchgr.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CHANGER_PRODUCT_DATA
req.alt-loc: ntddchgr.h
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
ms.keywords: CHANGER_PRODUCT_DATA, CHANGER_PRODUCT_DATA, *PCHANGER_PRODUCT_DATA
req.iface: 
---

# CHANGER_PRODUCT_DATA structure



## -description
<p>The CHANGER_PRODUCT_DATA structure is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559402">IOCTL_CHANGER_GET_PRODUCT_DATA</a> request to retrieve product data for a device. </p>


## -syntax

````
typedef struct _CHANGER_PRODUCT_DATA {
  UCHAR VendorId[VENDOR_ID_LENGTH];
  UCHAR ProductId[PRODUCT_ID_LENGTH];
  UCHAR Revision[REVISION_LENGTH];
  UCHAR SerialNumber[SERIAL_NUMBER_LENGTH];
  UCHAR DeviceType;
} CHANGER_PRODUCT_DATA, *PCHANGER_PRODUCT_DATA;
````


## -struct-fields
<dl>

### -field <b>VendorId</b>

<dd>
<p>Specifies the name of the device manufacturer. </p>
</dd>

### -field <b>ProductId</b>

<dd>
<p>Specifies the product identification as defined by the vendor.</p>
</dd>

### -field <b>Revision</b>

<dd>
<p>Specifies the product revision as defined by the vendor.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>Specifies the value defined by the vendor to identify this device. Serial numbers are unique for all changers of a given type, but are not necessarily unique across vendor and product lines. For a SCSI changer, this value might be from Vital Product Data. If <b>SerialNumber</b> is not unique, the miniclass driver should not set the CHANGER_SERIAL_NUMBER_VALID flag in the <b>Features0</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a> structure. </p>
</dd>

### -field <b>DeviceType</b>

<dd>
<p>Specifies the device type of the changer. This member must be MEDIUM_CHANGER.</p>
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
<dt>Ntddchgr.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559402">IOCTL_CHANGER_GET_PRODUCT_DATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551427">ChangerGetProductData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554979">GET_CHANGER_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20CHANGER_PRODUCT_DATA structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
