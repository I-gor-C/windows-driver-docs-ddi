---
UID: NS.ksmedia._DDVIDEOPORTCONNECT
title: DDVIDEOPORTCONNECT
author: windows-driver-content
description: The DDVIDEOPORTCONNECT structure describes a hardware video port connection.
old-location: display\ddvideoportconnect.htm
old-project: display
ms.assetid: 54c1bb05-37a8-4841-808b-2eb9d1ecd7a3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DDVIDEOPORTCONNECT, DDVIDEOPORTCONNECT, *LPDDVIDEOPORTCONNECT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: Dvp.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DDVIDEOPORTCONNECT
req.alt-loc: ksmedia.h
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

# DDVIDEOPORTCONNECT structure



## -description
<p>The DDVIDEOPORTCONNECT structure describes a hardware video port connection.</p>


## -syntax

````
typedef struct _DDVIDEOPORTCONNECT {
  DWORD     dwSize;
  DWORD     dwPortWidth;
  GUID      guidTypeID;
  DWORD     dwFlags;
  ULONG_PTR dwReserved1;
} DDVIDEOPORTCONNECT;
````


## -struct-fields
<dl>

### -field dwSize

<dd>
<p>Specifies the size in bytes of the DDVIDEOPORTCONNECT structure.</p>
</dd>

### -field dwPortWidth

<dd>
<p>Specifies the width of the hardware video port. This value represents the number of physical pins on the hardware video port. This member must always be filled in, even when the <b>guidTypeID</b> assumes a certain size. </p>
</dd>

### -field guidTypeID

<dd>
<p>Specifies a GUID that describes the synchronization characteristics of the hardware video port. The following port types are predefined:</p>
<table>
<tr>
<th>Port Type</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>DDVPTYPE_E_HREFH_VREFH</p>
</td>
<td>
<p>External syncs where HREF is active high and VREF is active high.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_E_HREFH_VREFL</p>
</td>
<td>
<p>External syncs where HREF is active high and VREF is active low.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_E_HREFL_VREFH</p>
</td>
<td>
<p>External syncs where HREF is active low and VREF is active high.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_E_HREFL_VREFL</p>
</td>
<td>
<p>External syncs where HREF is active low and VREF is active low.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_BROOKTREE</p>
</td>
<td>
<p>Sync information is embedded in the data stream using the Brooktree definition.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_CCIR656</p>
</td>
<td>
<p>Sync information is embedded in the data stream according to the CCIR656 specification.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPTYPE_PHILIPS</p>
</td>
<td>
<p>Sync information is embedded in the data stream using the Philips definition.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwFlags

<dd>
<p>Specifies a set of flags that identify the capabilities of the hardware video port connection. This member can be a bitwise OR of any of the following flags:</p>
<table>
<tr>
<th>Flag</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>DDVPCONNECT_DISCARDSVREFDATA</p>
</td>
<td>
<p>The device discards any data written during the VREF period, causing this data to not be written to the frame buffer. This flag should be set only by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_DOUBLECLOCK</p>
</td>
<td>
<p>When set by the driver, this flag indicates that the hardware video port is capable of double clocking the data. When set by the client, it indicates that the hardware video port should double clock the data. This flag is valid only in a hardware video port with a <b>guidTypeID</b> that supports an external sync.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_HALFLINE</p>
</td>
<td>
<p>When set by the driver, this flag indicates that the hardware video port supports writing half lines into the frame buffer, sometimes causing the data to not be displayed correctly. When set by the client, it indicates that the driver may write half lines.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_INTERLACED</p>
</td>
<td>
<p>When set by the driver, this flag indicates that the hardware video port supports interlaced signals. When set by the client, it indicates that the signal is interlaced.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_INVERTPOLARITY</p>
</td>
<td>
<p>When set by the driver, this flag indicates that the hardware video port is capable of inverting the field polarities; that is, treating even fields as odd and vice versa. When set by the client, it indicates that the hardware video port should invert the field polarities.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_SHAREEVEN</p>
</td>
<td>
<p>This is currently an unimplemented feature and should be ignored by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_SHAREODD</p>
</td>
<td>
<p>This is currently an unimplemented feature and should be ignored by the driver.</p>
</td>
</tr>
<tr>
<td>
<p>DDVPCONNECT_VACT</p>
</td>
<td>
<p>When set by the driver, this flag indicates that the hardware video port is capable of using an external VACT signal. When set by the client, it indicates that the hardware video port should use the external VACT signal.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field dwReserved1

<dd>
<p>Reserved for system use and should be set to zero. </p>
</dd>
</dl>

## -remarks
<p>The driver's <a href="display.ddvideoportgetconnectinfo">DdVideoPortGetConnectInfo</a> callback routine initializes a DDVIDEOPORTCONNECT structure for every connection that the hardware video port supports. The client can change the <b>dwFlags</b> member of one of the driver's DDVIDEOPORTCONNECT structures before calling the driver's <a href="display.ddvideoportcancreate">DdVideoPortCanCreate</a> callback.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h (include Dvp.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="display.ddvideoportcancreate">DdVideoPortCanCreate</a>
</dt>
<dt>
<a href="display.ddvideoportgetconnectinfo">DdVideoPortGetConnectInfo</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DDVIDEOPORTCONNECT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
