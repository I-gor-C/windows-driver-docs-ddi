---
UID: NS.winbio_types._WINBIO_BIR_HEADER
title: WINBIO_BIR_HEADER
author: windows-driver-content
description: The WINBIO_BIR_HEADER structure contains the Common Biometric Exchange File Format (CBEFF) Patron Format A information that describes the rest of the BIR.
old-location: biometric\winbio_bir_header.htm
old-project: biometric
ms.assetid: 5053b027-61a9-463a-967c-9e9ff1673b1c
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_BIR_HEADER, WINBIO_BIR_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winbio_types.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_BIR_HEADER
req.alt-loc: winbio_types.h
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
req.iface: IWiaTransferCallback
req.product: Windows 10 or later.
---

# WINBIO_BIR_HEADER structure



## -description
<p>The WINBIO_BIR_HEADER structure contains the Common Biometric Exchange File Format (CBEFF) Patron Format A information that describes the rest of the BIR.</p>


## -syntax

````
typedef struct _WINBIO_BIR_HEADER {
  USHORT                   ValidFields;
  WINBIO_BIR_VERSION       HeaderVersion;
  WINBIO_BIR_VERSION       PatronHeaderVersion;
  WINBIO_BIR_DATA_FLAGS    DataFlags;
  WINBIO_BIOMETRIC_TYPE    Type;
  WINBIO_BIOMETRIC_SUBTYPE Subtype;
  WINBIO_BIR_PURPOSE       Purpose;
  WINBIO_BIR_QUALITY       DataQuality;
  LARGE_INTEGER            CreationDate;
  struct {
    LARGE_INTEGER BeginDate;
    LARGE_INTEGER EndDate;
  } ValidityPeriod;
  WINBIO_REGISTERED_FORMAT BiometricDataFormat;
  WINBIO_REGISTERED_FORMAT ProductId;
} WINBIO_BIR_HEADER, *PWINBIO_BIR_HEADER;
````


## -struct-fields
<dl>

### -field <b>ValidFields</b>

<dd>
<p>A Patron Format A bitmask that indicates which CBEFF optional fields are present in the BIR. For more information about all members of WINBIO_BIR_HEADER, follow the link in the Remarks section to the <i>NISTIR 6529-A Specification</i>. </p>
</dd>

### -field <b>HeaderVersion</b>

<dd>
<p>A structure of type WINBIO_BIR_VERSION that specifies the CBEFF header version.</p>
<p>Versions are represented as 8-bit values of the form: 0x<i>NM</i>, where <i>N</i> is the major version and <i>M</i> is the minor version.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef UCHAR WINBIO_BIR_VERSION, *PWINBIO_BIR_VERSION;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>PatronHeaderVersion</b>

<dd>
<p>A structure of type WINBIO_BIR_VERSION that specifies PATRON_HEADER_VERSION.</p>
</dd>

### -field <b>DataFlags</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536461">WINBIO_BIR_DATA_FLAGS</a> that specifies the level of processing expected for a data capture.</p>
</dd>

### -field <b>Type</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536458">WINBIO_BIOMETRIC_TYPE</a> that specifies the biometric type.</p>
</dd>

### -field <b>Subtype</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536457">WINBIO_BIOMETRIC_SENSOR_SUBTYPE</a> that specifies the biometric subtype.</p>
</dd>

### -field <b>Purpose</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536463">WINBIO_BIR_PURPOSE</a> that specifies the intended use of the data.</p>
</dd>

### -field <b>DataQuality</b>

<dd>
<p>A structure of type WINBIO_BIR_QUALITY that specifies the biometric data quality. Quality measurements are represented as signed integers in the range 0-100, except:</p>
<p>-1  Quality measurements are supported by the BIR creator, but no value is set in the BIR.</p>
<p>-2  Quality measurements are not supported by the BIR creator.</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef CHAR WINBIO_BIR_QUALITY, *PWINBIO_BIR_QUALITY;</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>CreationDate</b>

<dd>
<p>Specifies the creation date and time of this BIR in UTC by using the format YYYYMMDDhhmmss.</p>
</dd>

### -field <b>ValidityPeriod</b>

<dd>
<p>Specifies the validity period of this BIR by using the format described in <i>CreationDate</i>.</p>
</dd>

### -field <b>BiometricDataFormat</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536473">WINBIO_REGISTERED_FORMAT</a> that specifies the data format of the <b>StandardDataBlock</b> for this <a href="https://msdn.microsoft.com/library/windows/hardware/ff536459">WINBIO_BIR</a>.</p>
</dd>

### -field <b>ProductId</b>

<dd>
<p>A structure of type <a href="https://msdn.microsoft.com/library/windows/hardware/ff536473">WINBIO_REGISTERED_FORMAT</a> that specifies the product identifier for the component that generated the <b>StandardDataBlock</b> for this WINBIO_BIR.</p>
</dd>
</dl>

## -remarks
<p>You can find more information about the fields of the standard biometric header in the <a href="http://go.microsoft.com/fwlink/p/?linkid=133328">NISTIR 6529-A Specification</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winbio_types.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536459">WINBIO_BIR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536460">WINBIO_BIR_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_BIR_HEADER structure%20 RELEASE:%20(11/13/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
