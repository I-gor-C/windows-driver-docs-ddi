---
UID: NS.drmk.tagDRMRIGHTS
title: tagDRMRIGHTS
author: windows-driver-content
description: The DRMRIGHTS structure specifies the DRM content rights assigned to a KS audio pin or to a port-class driver's stream object.
old-location: audio\drmrights.htm
old-project: audio
ms.assetid: 890f996c-9216-4148-b198-538963101c2a
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: tagDRMRIGHTS, DRMRIGHTS, *PDRMRIGHTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: drmk.h
req.include-header: Drmk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRMRIGHTS
req.alt-loc: drmk.h
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
req.iface: IDrmAudioStream
---

# tagDRMRIGHTS structure



## -description
<p>The <b>DRMRIGHTS</b> structure specifies the DRM content rights 
   assigned to a KS audio pin or to a port-class driver's stream object.</p>


## -syntax

````
typedef struct tagDRMRIGHTS {
  BOOL  CopyProtect;
  ULONG Reserved;
  BOOL  DigitalOutputDisable;
} DRMRIGHTS, *PDRMRIGHTS;
````


## -struct-fields
<dl>

### -field <b>CopyProtect</b>

<dd>
<p>Specifies one of the following copy-protection values:
	   </p>
<p></p>
<dl>

### -field <a id="TRUE"></a><a id="true"></a>TRUE

<dd>
<p>Enables copy protection. An audio application must not do the following:
		   </p>
<ul>
<li>
<p>Store the content in any form in any nonvolatile storage.</p>
</li>
<li>
<p>Pass the content by reference or by value to any other component within the host system that is not 
			   authenticated by the DRM system.</p>
</li>
</ul>
</dd>

### -field <a id="FALSE"></a><a id="false"></a>FALSE

<dd>
<p>Disables copy protection. Content can be copied without restrictions.</p>
</dd>
</dl>
<p>For more information about <b>CopyProtect</b>, see the Remarks section.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use. Initialize to zero.</p>
</dd>

### -field <b>DigitalOutputDisable</b>

<dd>
<p>Specifies one of the following digital output protection values:</p>
<p></p>
<dl>

### -field <a id="TRUE"></a><a id="true"></a>TRUE

<dd>
<p>Disable digital outputs. A software component must not transfer the content out of the host system through any type of digital interface. Note that digital output protection does not affect USB devices because the host system includes USB devices.</p>
</dd>

### -field <a id="FALSE"></a><a id="false"></a>FALSE

<dd>
<p>Enables digital outputs. Content can be transferred from the host system to an external component without restrictions.</p>
</dd>
</dl>
<p>For more information about <b>DigitalOutputDisable</b>, see the Remarks section.</p>
</dd>
</dl>

## -remarks
<p>The Windows Certification Program places specific requirements on the way an audio driver handles the <b>CopyProtect</b> and <b>DigitalOutputDisable</b> values. These requirements are applicable when the <b>CopyProtect</b> and <b>DigitalOutputDisable</b> values are applied to an audio stream and to the output from which the audio stream is accessed. New requirements for Windows 7 include the correct way to program the serial copy management system (SCMS) for S/PDIF endpoints, and high-bandwidth digital content protection (HDCP) for HDMI endpoints.</p>

<p>The following table summarizes the content protection state that the driver must establish for different values of <b>CopyProtect</b> and <b>DigitalOutputDisable</b>.</p>

<p><b>DRMRIGHTS Boolean members</b></p>

<p><b>Resulting content protection</b></p>

<p><b>DigitalOutputDisable</b></p>

<p><b>CopyProtect</b></p>

<p><b>
        HDMI and Display port</b></p>

<p><b>S/PDIF</b></p>

<p>False</p>

<p>False</p>

<p>Enabled with no HDCP</p>

<p>Enabled with no SCMS</p>

<p>False</p>

<p>True</p>

<p>Enabled with HDCP</p>

<p>Enabled with SCMS</p>

<p>True</p>

<p>Don't care</p>

<p>Enabled with HDCP</p>

<p>Disabled</p>

<p> </p>

<p>When an audio driver applies SCMS copy protection to a S/PDIF endpoint, the audio driver uses a combination of the L, Cp, and Category Code bits to select an SCMS state of "Copy Never." For more information about copy protection for digital content, see <a href="http://go.microsoft.com/fwlink/p/?linkid=158256">IEC 60958</a> on the IEC website.</p>

<p>If the driver supports DRMRIGHTS and also implements a proprietary copy protection mechanism, the driver must aggregate the result of the proprietary implementation with the values of <b>CopyProtect</b> and <b>DigitalOutputDisable</b> to determine the final copy protection state. The final copy protection state must be the most restrictive of all outstanding copy protection requests. </p>

<p>The <b>DEFINE_DRMRIGHTS_DEFAULT</b> macro defines a constant <b>DRMRIGHTS</b> structure that specifies default DRM content rights.</p>

<p>Parameters</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Drmk.h (include Drmk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536348">DrmCreateContentMixed</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536349">DrmDestroyContent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536352">DrmForwardContentToFileObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536353">DrmForwardContentToInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536354">DrmGetContentRights</a>
</dt>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=158256">IEC 60958</a></dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20DRMRIGHTS structure%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
