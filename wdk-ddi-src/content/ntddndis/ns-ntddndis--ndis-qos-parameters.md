---
UID: NS.ntddndis._NDIS_QOS_PARAMETERS
title: NDIS_QOS_PARAMETERS
author: windows-driver-content
description: The NDIS_QOS_PARAMETERS structure specifies the NDIS Quality of Service (QoS) parameters that are enabled on a network adapter that supports the IEEE 802.1 Data Center Bridging (DCB) interface.
old-location: netvista\ndis_qos_parameters.htm
ms.assetid: 83eb72a8-d35b-445d-a207-c14a3bedd308
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_QOS_PARAMETERS
req.alt-loc: Ntddndis.h
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
ms.keywords: NDIS_QOS_PARAMETERS, NDIS_QOS_PARAMETERS, *PNDIS_QOS_PARAMETERS
req.iface: 
---

# NDIS_QOS_PARAMETERS structure



## -description
<p>
<p>The <b>NDIS_QOS_PARAMETERS</b> structure specifies the NDIS Quality of Service (QoS) parameters that are enabled on a network adapter that supports the IEEE 802.1 Data Center Bridging (DCB) interface.</p>
</p>
<p>The <b>NDIS_QOS_PARAMETERS</b> structure specifies the NDIS Quality of Service (QoS) parameters that are enabled on a network adapter that supports the IEEE 802.1 Data Center Bridging (DCB) interface.</p>


## -syntax

````
typedef struct _NDIS_QOS_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              Flags;
  ULONG              NumTrafficClasses;
  UCHAR              PriorityAssignmentTable[NDIS_QOS_MAXIMUM_PRIORITIES];
  UCHAR              TcBandwidthAssignmentTable[NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES];
  UCHAR              TsaAssignmentTable[NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES];
  ULONG              PfcEnable;
  ULONG              NumClassificationElements;
  ULONG              ClassificationElementSize;
  ULONG              FirstClassificationElementOffset;
} NDIS_QOS_PARAMETERS, *PNDIS_QOS_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_QOS_PARAMETERS</b> structure. This member is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_QOS_PARAMETERS. To specify the version of the <b>NDIS_QOS_PARAMETERS</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_QOS_PARAMETERS_REVISION_1"></a><a id="ndis_qos_parameters_revision_1"></a>NDIS_QOS_PARAMETERS_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_QOS_PARAMETERS_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags that specify the status of the NDIS QoS parameters for the network adapter. For more information about this member, see <a href="#overview">Overview of the Flags Member</a>.</p>
</dd>

### -field <b>NumTrafficClasses</b>

<dd>
<p>A <b>ULONG</b> value that specifies the number of NDIS QoS traffic classes that are enabled on the network adapter.  Each traffic class is referenced through an identifier in the range from zero to (<b>NumTrafficClasses</b>–1).</p>
<div class="alert"><b>Note</b>  The value of the <b>NumTrafficClasses</b> member must be less than or equal to <b>min</b>(<b>NDIS_QOS_MAXIMUM_TRAFFIC_CLASSES</b>, <i>MaxNumTrafficClasses</i>), where <i>MaxNumTrafficClasses</i> is the value of the <b>MaxNumTrafficClasses</b> member that was specified  in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451629">NDIS_QOS_CAPABILITIES</a> structure.</div>
<div> </div>
</dd>

### -field <b>PriorityAssignmentTable</b>

<dd>
<p>An array of <b>UCHAR</b> elements that specifies an IEEE 802.1p priority level for each traffic class. The <b>PriorityAssignmentTable</b> array is indexed  by the  802.1p priority level (0–7). </p>
<p>Each element contains the traffic class identifier. This identifier is the index of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451631">NDIS_QOS_CLASSIFICATION_ELEMENT</a> structure for the traffic class within the classification array.</p>
<div class="alert"><b>Note</b>  Each element in the <b>PriorityAssignmentTable</b> array must be assigned a valid traffic class identifier. A traffic class identifier can be assigned to more than one element in the <b>PriorityAssignmentTable</b> array.</div>
<div> </div>
</dd>

### -field <b>TcBandwidthAssignmentTable</b>

<dd>
<p>An array of <b>UCHAR</b> elements that specifies the percentage of the bandwidth allocation assigned to each traffic class. The <b>TcBandwidthAssignmentTable</b> array is indexed by the   traffic class identifier. </p>
<p>Each element of the <b>TcBandwidthAssignmentTable</b> array specifies the bandwidth allocation for the traffic classes. The total value of all bandwidth allocation assignments  in the <b>TcBandwidthAssignmentTable</b> array must equal 100.</p>
<div class="alert"><b>Note</b>  Bandwidth allocation is supported only for the Enhanced Transmission Selection (ETS) TSA. If the element for the traffic class in the <b>TsaAssignmentTable</b> array is not set to NDIS_QOS_TSA_ETS, the element for the traffic class in the <b>TcBandwidthAssignmentTable</b> array must be set to zero.</div>
<div> </div>
</dd>

### -field <b>TsaAssignmentTable</b>

<dd>
<p>An array of <b>UCHAR</b> elements that specifies the TSA assigned to each traffic class. The <b>TsaAssignmentTable</b> array is indexed by the   traffic class identifier. </p>
<p>Each element of the <b>TsaAssignmentTable</b> array contains one of the following values:</p>
<p></p>
<dl>

### -field <a id="NDIS_QOS_TSA_STRICT"></a><a id="ndis_qos_tsa_strict"></a>NDIS_QOS_TSA_STRICT

<dd>
<p>The strict priority algorithm must be used as the TSA for the traffic class. For more information about this TSA, see <a href="NULL">Strict Priority Algorithm</a>.</p>
</dd>

### -field <a id="NDIS_QOS_TSA_CBS"></a><a id="ndis_qos_tsa_cbs"></a>NDIS_QOS_TSA_CBS

<dd>
<p>The IEEE 802.1Qav credit-based shaper (CBS) algorithm must be used as the TSA for the traffic class.</p>
<div class="alert"><b>Note</b>  Starting with Windows Server 2012, the DCB component (Msdcb.sys) does not support the CBS TSA and won't enable this parameter through object identifier (OID) method requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451835">OID_QOS_PARAMETERS</a>. For more information on the DCB component, see <a href="NULL">NDIS QoS Architecture for Data Center Bridging</a>.</div>
<div> </div>
</dd>

### -field <a id="NDIS_QOS_TSA_ETS"></a><a id="ndis_qos_tsa_ets"></a>NDIS_QOS_TSA_ETS

<dd>
<p>The IEEE 802.1Qaz Enhanced Transmission Selection (ETS) algorithm must be used as the TSA for the traffic class. For more information about this TSA, see <a href="NULL">Enhanced Transmission Selection (ETS) Algorithm</a>.</p>
</dd>
</dl>
</dd>

### -field <b>PfcEnable</b>

<dd>
<p>A bitmap of 32 bits. The most-significant 24 bits are reserved for future use. The least-significant 8 bits are used to specify whether PFC
is enabled on the IEEE 802.1p priority level. If the bit is set to one, PFC is enabled for the priority level.</p>
<table>
<tr>
<th>Bit range</th>
<th>Meaning</th>
</tr>
<tr>
<td>31:24</td>
<td>Reserved for future use.</td>
</tr>
<tr>
<td>7</td>
<td>If set to one, PFC is enabled on 802.1p priority level 7 (<i>network control</i>).</td>
</tr>
<tr>
<td>6</td>
<td>If set to one, PFC is enabled on 802.1p priority level 6 (<i>internetwork control</i>).</td>
</tr>
<tr>
<td>5</td>
<td>If set to one, PFC is enabled on 802.1p priority level 5 (<i>voice</i>).</td>
</tr>
<tr>
<td>4</td>
<td>If set to one, PFC is enabled on 802.1p priority level 4 (<i>video</i>).</td>
</tr>
<tr>
<td>3</td>
<td>If set to one, PFC is enabled on 802.1p priority level 3 (<i>critical applications</i>).</td>
</tr>
<tr>
<td>2</td>
<td>If set to one, PFC is enabled on 802.1p priority level 2 (<i>excellent effort</i>).</td>
</tr>
<tr>
<td>1</td>
<td>If set to one, PFC is enabled on 802.1p priority level 1 (<i>background</i>).</td>
</tr>
<tr>
<td>0</td>
<td>If set to one, PFC is enabled on 802.1p priority level 0 (<i>best effort</i>).</td>
</tr>
</table>
<p> </p>
<div class="alert"><b>Note</b>  The total number of 802.1p priority levels that have PFC enabled must be less than or equal to the value of the <b>MaxNumPfcEnabledTrafficClasses</b> member in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451629">NDIS_QOS_CAPABILITIES</a> structure.</div>
<div> </div>
<p>For more information about priority levels, see <a href="NULL">IEEE 802.1p Priority Levels</a>.</p>
</dd>

### -field <b>NumClassificationElements</b>

<dd>
<p>A <b>ULONG</b> value that specifies the number of elements in the traffic classification array. The offset to the first element in this array is specified  by the <b>FirstClassificationElementOffset</b> member.</p>
<div class="alert"><b>Note</b>  Each element in the array is formatted as an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451631">NDIS_QOS_CLASSIFICATION_ELEMENT</a> structure.</div>
<div> </div>
</dd>

### -field <b>ClassificationElementSize</b>

<dd>
<p>A <b>ULONG</b> value that specifies the size, in bytes, of each element in the traffic classification array.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, this member must be set  to <code>sizeof(NDIS_QOS_CLASSIFICATION_ELEMENT</code>).</div>
<div> </div>
</dd>

### -field <b>FirstClassificationElementOffset</b>

<dd>
<p>A <b>ULONG</b> value that specifies the offset, in bytes, to the first element in an array of traffic classification elements that follow this structure. The offset is measured from the start of the <b>NDIS_QOS_PARAMETERS</b> structure up to the beginning of the first element. Each element in the array is an <a href="https://msdn.microsoft.com/library/windows/hardware/hh451631">NDIS_QOS_CLASSIFICATION_ELEMENT</a> structure.

</p>
<div class="alert"><b>Note</b>  If <b>NumClassificationElements</b> is set to zero, this member is ignored.  </div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_QOS_PARAMETERS</b> structure specifies the parameters that define how the network adapter prioritizes transmit, or <i>egress</i>, packets. This structure is used in the following OID requests:</p>

<p>OID query request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451832">OID_QOS_OPERATIONAL_PARAMETERS</a>.  This OID request returns the operational QoS parameters that are currently provisioned on the network adapter.</p>

<p>OID query request of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451841">OID_QOS_REMOTE_PARAMETERS</a>. This OID request returns the remote QoS parameters that are currently provisioned on the network adapter.</p>

<p>OID method requests of <a href="https://msdn.microsoft.com/library/windows/hardware/hh451835">OID_QOS_PARAMETERS</a>. This OID request provisions the network adapter with the local QoS parameters.</p>

<p>The miniport driver also returns an <b>NDIS_QOS_PARAMETERS</b> structure  in the following NDIS status indications:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439810">NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE</a>. This miniport driver issues this status indication when its operational QoS parameters change.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439812">NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE</a>. This miniport driver issues this status indication when its remote QoS parameters change.</p>

<p> For more information about the types of NDIS QoS parameters, see <a href="NULL">Overview of NDIS QoS Parameters</a>.</p>

<p>The <b>Flags</b> member contains a bitwise <b>OR</b> of flags that specify the status of the NDIS QoS parameters for the network adapter. </p>

<p>The miniport driver sets the <b>Flags</b> member when it issues the following NDIS status indications:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439810">NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439812">NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE</a>
</p>

<p>The DCB component sets the <b>Flags</b> member when it issues an OID method request of  <a href="https://msdn.microsoft.com/library/windows/hardware/hh451835">OID_QOS_PARAMETERS</a>.</p>

<p>The following flags are defined for the <b>Flags</b> member.</p>

<p></p><dl>
<dt><a id="NDIS_QOS_PARAMETERS_ETS_CONFIGURED"></a><a id="ndis_qos_parameters_ets_configured"></a><b>NDIS_QOS_PARAMETERS_ETS_CONFIGURED</b></dt>
<dd>
<p>If this flag is set, the miniport driver has configured the network adapter with the ETS parameters contained in the following members:</p>
<ul>
<li>
<p><b>NumTrafficClasses</b></p>
</li>
<li>
<p><b>PriorityAssignmentTable</b></p>
</li>
<li>
<p><b>TcBandwidthAssignmentTable</b></p>
</li>
<li>
<p><b>TsaAssignmentTable</b></p>
</li>
</ul>
<div class="alert"><b>Note</b>  The miniport driver must support ETS in order to support NDIS QoS for DCB. However, the setting of this flag does not specify whether the network adapter supports ETS. Instead, the setting of this flag specifies only whether ETS parameters are configured on the network adapter.</div>
<div> </div>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_ETS_CHANGED"></a><a id="ndis_qos_parameters_ets_changed"></a><b>NDIS_QOS_PARAMETERS_ETS_CHANGED</b></dt>
<dd>
<p>If this flag is set, one or more ETS parameters have changed in the following members:</p>
<ul>
<li>
<p><b>NumTrafficClasses</b></p>
</li>
<li>
<p><b>PriorityAssignmentTable</b></p>
</li>
<li>
<p><b>TcBandwidthAssignmentTable</b></p>
</li>
<li>
<p><b>TsaAssignmentTable</b></p>
</li>
</ul>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_PFC_CONFIGURED"></a><a id="ndis_qos_parameters_pfc_configured"></a><b>NDIS_QOS_PARAMETERS_PFC_CONFIGURED</b></dt>
<dd>
<p>If this flag is set, the miniport driver has configured the network adapter with the   PFC settings contained in the  <b>PfcEnable</b> member.</p>
<div class="alert"><b>Note</b>  The miniport driver must support PFC in order to support NDIS QoS for DCB. The setting of this flag does not specify whether the network adapter supports PFC. Instead, the setting of this flag specifies only whether PFC parameters are enabled on the network adapter.</div>
<div> </div>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_PFC_CHANGED"></a><a id="ndis_qos_parameters_pfc_changed"></a><b>NDIS_QOS_PARAMETERS_PFC_CHANGED</b></dt>
<dd>
<p>If this flag is set, one or more PFC settings have changed in the  <b>PfcEnable</b> member.</p>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_CLASSIFICATION_CONFIGURED"></a><a id="ndis_qos_parameters_classification_configured"></a><b>NDIS_QOS_PARAMETERS_CLASSIFICATION_CONFIGURED</b></dt>
<dd>
<p>If this flag is set, the miniport driver has configured the network adapter with the QoS traffic classification parameters specified in the following members:</p>
<ul>
<li>
<p><b>NumClassificationElements</b></p>
</li>
<li>
<p><b>ClassificationElementSize</b></p>
</li>
<li>
<p><b>FirstClassificationElementOffset</b></p>
</li>
</ul>
<div class="alert"><b>Note</b>  It is possible for the <b>NDIS_QOS_PARAMETERS_CLASSIFICATION_CONFIGURED</b> not to be set even if the <b>NDIS_QOS_PARAMETERS_ETS_CONFIGURED</b> and <b>NDIS_QOS_PARAMETERS_PFC_CONFIGURED</b> flags are set. In this case, the miniport driver must not configure QoS traffic classifications by using its proprietary settings that are defined by the independent hardware vendor (IHV).</div>
<div> </div>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_CLASSIFICATION_CHANGED"></a><a id="ndis_qos_parameters_classification_changed"></a><b>NDIS_QOS_PARAMETERS_CLASSIFICATION_CHANGED</b></dt>
<dd>
<p>If this flag is set, one or more QoS traffic classification parameters have changed in the following members:</p>
<ul>
<li>
<p><b>NumClassificationElements</b></p>
</li>
<li>
<p><b>ClassificationElementSize</b></p>
</li>
<li>
<p><b>FirstClassificationElementOffset</b></p>
</li>
</ul>
</dd>
<dt><a id="NDIS_QOS_PARAMETERS_WILLING"></a><a id="ndis_qos_parameters_willing"></a><b>NDIS_QOS_PARAMETERS_WILLING</b></dt>
<dd>
<p>This flag specifies whether the miniport driver enables or disables the  local Data Center Bridging Exchange (DCBX) Willing state. The driver handles this flag in the following way:</p>
<ul>
<li>
<p>If this flag is set, the miniport driver must enable the local DCBX Willing state. This allows the driver to be remotely configured with QoS settings. In this case, the driver resolves its operational QoS parameters based on the remote QoS parameters.
The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the IHV.</p>
</li>
<li>
<p>If this flag is not set, the miniport driver must disable the local DCBX Willing state. This allows the driver to resolve its operational QoS parameters from its local QoS parameters instead of remote QoS parameters.
The miniport driver must also disable or override any local QoS parameter for which the related <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CONFIGURED</b> flag is not set. </p>
<p>For example, the miniport driver can override an unconfigured local QoS parameter with its proprietary settings for the QoS parameters that are defined by the IHV. If there are no proprietary settings for  local QoS parameters that are not specified with an  <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CONFIGURED</b> flag, the driver must disable the use of these QoS parameters on the network adapter.</p>
</li>
</ul>
<p>For more information about the local DCBX Willing state, see <a href="NULL">Managing the Local DCBX Willing State</a>.

</p>
<div class="alert"><b>Note</b>  This flag is reserved for NDIS. The miniport driver must not set this flag when it issues <b>NDIS_STATUS_QOS_<i>Xxx</i></b> status indications.</div>
<div> </div>
</dd>
</dl><p>If this flag is set, the miniport driver has configured the network adapter with the ETS parameters contained in the following members:</p>

<p><b>NumTrafficClasses</b></p>

<p><b>PriorityAssignmentTable</b></p>

<p><b>TcBandwidthAssignmentTable</b></p>

<p><b>TsaAssignmentTable</b></p>

<p>If this flag is set, one or more ETS parameters have changed in the following members:</p>

<p><b>NumTrafficClasses</b></p>

<p><b>PriorityAssignmentTable</b></p>

<p><b>TcBandwidthAssignmentTable</b></p>

<p><b>TsaAssignmentTable</b></p>

<p>If this flag is set, the miniport driver has configured the network adapter with the   PFC settings contained in the  <b>PfcEnable</b> member.</p>

<p>If this flag is set, one or more PFC settings have changed in the  <b>PfcEnable</b> member.</p>

<p>If this flag is set, the miniport driver has configured the network adapter with the QoS traffic classification parameters specified in the following members:</p>

<p><b>NumClassificationElements</b></p>

<p><b>ClassificationElementSize</b></p>

<p><b>FirstClassificationElementOffset</b></p>

<p>If this flag is set, one or more QoS traffic classification parameters have changed in the following members:</p>

<p><b>NumClassificationElements</b></p>

<p><b>ClassificationElementSize</b></p>

<p><b>FirstClassificationElementOffset</b></p>

<p>This flag specifies whether the miniport driver enables or disables the  local Data Center Bridging Exchange (DCBX) Willing state. The driver handles this flag in the following way:</p>

<p>If this flag is set, the miniport driver must enable the local DCBX Willing state. This allows the driver to be remotely configured with QoS settings. In this case, the driver resolves its operational QoS parameters based on the remote QoS parameters.
The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the IHV.</p>

<p>If this flag is not set, the miniport driver must disable the local DCBX Willing state. This allows the driver to resolve its operational QoS parameters from its local QoS parameters instead of remote QoS parameters.
The miniport driver must also disable or override any local QoS parameter for which the related <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CONFIGURED</b> flag is not set. </p>

<p>For example, the miniport driver can override an unconfigured local QoS parameter with its proprietary settings for the QoS parameters that are defined by the IHV. If there are no proprietary settings for  local QoS parameters that are not specified with an  <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CONFIGURED</b> flag, the driver must disable the use of these QoS parameters on the network adapter.</p>

<p>For more information about the local DCBX Willing state, see <a href="NULL">Managing the Local DCBX Willing State</a>.

</p>

<p>The <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CHANGED</b> flags provide hints as to whether the corresponding group of parameters has changed from a previous <a href="https://msdn.microsoft.com/library/windows/hardware/hh451835">OID_QOS_PARAMETERS</a> method request  or <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CHANGED</b> status notification. When the miniport driver issues the <b>NDIS_QOS_PARAMETERS_<i>Xxx</i>_CHANGED</b> status notifications, it can  optionally set these flags.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565924">NDIS_MINIPORT_ADAPTER_HARDWARE_ASSIST_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
    NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451629">NDIS_QOS_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451631">NDIS_QOS_CLASSIFICATION_ELEMENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439810">NDIS_STATUS_QOS_OPERATIONAL_PARAMETERS_CHANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439812">NDIS_STATUS_QOS_REMOTE_PARAMETERS_CHANGE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451827">OID_QOS_CURRENT_CAPABILITIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451828">OID_QOS_HARDWARE_CAPABILITIES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_QOS_PARAMETERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
